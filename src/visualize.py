import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def prepare(test_face, image_rates, std_pc, mean):

    p_test = np.array(test_face).reshape(100, 100)

    p_mean = mean.reshape(100, 100)

    pix_std = _pixelize(std_pc)
    p_eigen = np.array(pix_std.iloc[:, 0]).reshape(100, 100)

    p_build = _build_face(image_rates, mean, pix_std)
    p_build = np.array(p_build).reshape(100, 100)

    return p_mean, p_test, p_eigen, p_build


def _pixelize(df):
    new_img = pd.DataFrame(MinMaxScaler().fit_transform(df))
    new_img = (new_img * 255).astype('int')
    return new_img


def _build_face(coeffs, mean, pixel_faces):
    acc = np.zeros(10000, dtype=int)
    for i in range(len(pixel_faces.columns)):
        term = float(coeffs[i]) * pixel_faces[i]
        acc = acc + term
    new_face = _pixelize(pd.DataFrame(acc + mean))
    return new_face
