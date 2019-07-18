import pandas as pd
import math
from .eigenfaces import calculate_rates

def _eucl(point, image_rates):
    s = (point - image_rates).pow(2)
    s = s.sum(axis=1)
    return math.sqrt(s)

def _multidim_knn(cd, image_rates):
    distance_from_chosen = []
    set_size = len(cd)
    for i in range(set_size):
        point = cd.iloc[i, 1:]
        d = _eucl(point, image_rates)
        distance_from_chosen.append(d)

    distance_from_chosen = pd.DataFrame({"face_class": cd["face_class"], "distance_from_chosen": distance_from_chosen})
    distance_from_chosen = distance_from_chosen.sort_values(by=['distance_from_chosen'])
    
    k = int(math.sqrt(set_size))
    if k % 2 == 0:
        k = k + 1
    distance_from_chosen = distance_from_chosen.iloc[:k]
    verdict = distance_from_chosen.face_class.mode()[0]
    return verdict
    

def classify(image, std_pc, mean, rates):
    dev = image.sub(mean, axis=0)
    image_rates = calculate_rates(std_pc, dev).transpose()
    verdict = _multidim_knn(rates, image_rates)
    return verdict, image_rates
