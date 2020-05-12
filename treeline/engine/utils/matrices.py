import numpy as np


def identity() -> np.array:
    return np.array([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])


def translate(v: np.array) -> np.array:
    return np.array([[1, 0, v[0]],
                     [0, 1, v[1]],
                     [0, 0, 1]])


def scale(s: np.array) -> np.array:
    return np.array([[s[0], 0, 0],
                     [0, s[1], 0],
                     [0, 0, 1]])
