import numpy as np
import pandas as pd
from sklearn.preprocessing import scale


def _calculate_pc(dev, ef_num):
    cov_matrix_smaller = dev.transpose().dot(dev)
    w, v = np.linalg.eig(cov_matrix_smaller)
    eigenvalues = pd.DataFrame(w, columns=['eigenvalue']).astype('int')
    eigenvector = pd.DataFrame(v)
    pc = dev.dot(eigenvector)
    comb = pd.concat([eigenvalues.transpose(), pc], axis=0)
    comb = comb.sort_values(axis=1, by=['eigenvalue'], ascending=False)
    pc = comb.iloc[:, 0:ef_num].drop(['eigenvalue'])
    return pc


def calculate_rates(std_pc, dev):
    rates = std_pc.transpose().dot(dev)
    rates = pd.DataFrame(scale(rates))
    return rates


def produce_eigenfaces(data, ef_num):
    mean = np.array(data.mean(axis=1)).astype('int')
    dev = data.sub(mean, axis=0)
    pc = _calculate_pc(dev, ef_num)
    std_pc = pd.DataFrame(scale(pc))
    rates = calculate_rates(std_pc, dev)
    return std_pc, mean, rates
