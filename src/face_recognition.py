
from .faceload import load_image, load_images
from .visualize import prepare
from .eigenfaces import produce_eigenfaces
from .classification import classify


def recognize(training_path, test_path, part):

    train_faces, classes_vector = load_images(training_path)
    test_face = load_image(image_path=test_path)

    ef_num = int(part*len(train_faces.columns))
    std_pc, mean, rates = produce_eigenfaces(train_faces, ef_num)
    rates = rates.transpose()
    rates.insert(loc=0, column="face_class", value=classes_vector)

    verdict, image_rates = classify(test_face, std_pc, mean, rates)

    p_mean, p_test, p_eigen, p_build = prepare(test_face, image_rates, std_pc, mean)

    return {"verdict": verdict, "mean": p_mean, "eigen": p_eigen, "test": p_test, "build": p_build}
