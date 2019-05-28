import glob
import os
import cv2
import pandas as pd
import numpy as np
from PIL import Image


def load_image(**kwargs):

    if "data" in kwargs:
        data = kwargs.get("data")
    else:
        data = pd.DataFrame(dtype=float)
    image_path = kwargs.get("image_path")

    pic = cv2.imread(image_path)
    pic = pic[:, :, 0]
    if pic.shape[0] > 100 or pic.shape[1] > 100:
        pic = format_image(pic, pic.shape[0], pic.shape[1])
    p = pd.DataFrame(pic.ravel().tolist(), dtype=float)
    data = pd.concat([data, p], axis=1, ignore_index=True)
    return data


def format_image(pic, height, width):
    size = 100, 100
    original = Image.fromarray(pic)

    if width < height:
        raise Exception("Wrong photo format.")
    left = int((width - height) / 2)
    if not (left % 2) == 0:
        left = left + 1
    top = 0
    right = width - left
    bottom = height
    cropped = original.crop((left, top, right, bottom))
    cropped.thumbnail(size)
    return np.array(cropped)


def load_images(dir_path):
    directories = glob.glob(dir_path + "/*")
    data = pd.DataFrame(dtype=float)
    classes_vector = []
    for directory in directories:
        images = glob.glob(directory + "/*")
        for image_path in images:

            data = load_image(image_path=image_path, data=data)
            classes_vector.append(os.path.basename(directory))

        print(len(images), "images loaded from", directory)
    return data, classes_vector
