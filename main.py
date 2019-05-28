from tkinter import *
from tkinter import font
from tkinter import filedialog
import FFR
import matplotlib.pyplot as plt

dict_answer = {}
default_path_1 = './datasets/google_photos/training_set'
default_path_2 = '.datasets/google_photos/testing_set/photoman1.jpg'


def go_event(rate_field, dict_answer_field, path_1, path_2):
    path_1 = path_1.get()
    path_2 = path_2.get()

    part = float(rate_field.get())
    if path_1 == "" or path_2 == "" or (part < 0.0 or part > 1.0):
        print("not yet")
    else:
        print(path_1)
        print(path_2)
        global dict_answer
        dict_answer = FFR.main(path_1, path_2, part)
        dict_answer_field.config(state='normal')
        dict_answer_field.delete(0, END)
        dict_answer_field.insert(0, dict_answer.get("verdict"))
        dict_answer_field.config(state='readonly')


def go_vis(key):
    if len(dict_answer) == 0:
        print("not yet")
    else:
        cv_img = dict_answer.get(key)
        plt.imshow(cv_img, cmap='gray')
        plt.show()


def browse(status_bar, image_needed):
    if image_needed:
        filename = filedialog.askopenfilename(title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    else:
        filename = filedialog.askdirectory()
    status_bar.config(state='normal')
    status_bar.delete(0, END)
    status_bar.insert(0, filename)
    status_bar.config(state='readonly')


def main():
    root = Tk()
    root.configure(background='white')
    root.geometry("1183x502")
    root.title("eigenfaces demo")

    ala = font.Font(family="Symbol", size=13)

    label_1 = Label(root, text="Training set:", font=ala, bg='white')
    status_1_message = StringVar()
    status_1 = Entry(root, relief=RIDGE, font=ala, textvariable=status_1_message, width=90)
    status_1.insert(0, default_path_1)
    status_1.config(state='readonly')

    label_2 = Label(root, text="Testing image:", font=ala, bg='white')
    status_2_message = StringVar()
    status_2 = Entry(root, relief=RIDGE, font=ala, textvariable=status_2_message, width=90)
    status_2.insert(0, default_path_2)
    status_2.config(state='readonly')

    search_button_1 = Button(root, text="Browse", command=lambda ar=status_1: browse(ar, False))
    search_button_2 = Button(root, text="Browse", command=lambda ar=status_2: browse(ar, True))

    label_3 = Label(root, text="Part of Training Set for Eigenfaces:", font=ala, bg='white')
    rate_field = Entry(root, relief=RIDGE, font=ala, width=3)
    rate_field.insert(0, "1")

    label_4 = Label(root, text="Answer:", font=ala, bg='white')
    verdict_message = StringVar()
    verdict_field = Entry(root, relief=RIDGE, font=ala, textvariable=verdict_message, width=90)
    verdict_field.config(state='readonly')

    go_button = Button(root, text="Start", command=lambda
        ar=rate_field,
        ar0=verdict_field,
        ar1=status_1_message,
        ar2=status_2_message: go_event(ar, ar0, ar1, ar2))

    test_button = Button(root, text="Show Test", command=lambda arg="test": go_vis(arg))
    mean_button = Button(root, text="Show Mean", command=lambda arg="mean": go_vis(arg))
    eigen_button = Button(root, text="Show Eigenfaces", command=lambda arg="eigen": go_vis(arg))
    build_button = Button(root, text="Build Face", command=lambda arg="build": go_vis(arg))

    label_1.grid(row=0, column=0, sticky="NESW", pady=4, padx=4)
    status_1.grid(row=1, column=0, sticky="NESW", pady=4, padx=4)
    search_button_1.grid(row=1, column=1, sticky="NESW", pady=4, padx=4)

    label_2.grid(row=2, column=0, sticky="NESW", pady=4, padx=4)
    status_2.grid(row=3, column=0, sticky="NESW", pady=4, padx=4)
    search_button_2.grid(row=3, column=1, sticky="NESW", pady=4, padx=4)

    label_3.grid(row=4, column=0, sticky="NESW", pady=4, padx=4)
    rate_field.grid(row=4, column=1, pady=4, padx=4)

    label_4.grid(row=5, column=0, sticky="NESW", pady=4, padx=4)
    go_button.grid(row=6, column=1, sticky="NESW", pady=4, padx=4)
    verdict_field.grid(row=6, column=0, sticky="NESW", pady=4, padx=4)

    test_button.grid(row=7, column=1, sticky="NESW", pady=4, padx=4)
    mean_button.grid(row=8, column=1, sticky="NESW", pady=4, padx=4)
    eigen_button.grid(row=10, column=1, sticky="NESW", pady=4, padx=4)
    build_button.grid(row=11, column=1, sticky="NESW", pady=4, padx=4)

    root.mainloop()


if __name__ == "__main__":
    main()
