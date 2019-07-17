import eigenfaces
import classification
import faceload
import visualize as ve


def recognize(training_path, test_path, part):

    train_faces, classes_vector = faceload.load_images(training_path)
    test_face = faceload.load_image(image_path=test_path)

    ef_num = int(part*len(train_faces.columns))
    std_pc, mean, rates = eigenfaces.produce_eigenfaces(train_faces, ef_num)
    rates = rates.transpose()
    rates.insert(loc=0, column="face_class", value=classes_vector)

    verdict, image_rates = classification.classify(test_face, std_pc, mean, rates)

    p_mean, p_test, p_eigen, p_build = ve.prepare(test_face, image_rates, std_pc, mean)

    return {"verdict": verdict, "mean": p_mean, "eigen": p_eigen, "test": p_test, "build": p_build}
