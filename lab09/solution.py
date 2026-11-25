import numpy as np

arr = np.array([12, 27, 19, 30])
arr[arr > 25] = 25       # маска с одним условием
fahrenheit = arr * 9 / 5 + 32


def make_hours(): # -> list[int]
    return np.arange(0, 21, 3)

def vector_report(values: list[float]): #  -> dict
    return {
        'third': values[2],
        'last': values[-1],
        'middle': values[2:6],
        'every_second': values[::2],
        'reversed': values[::-1],
        }

def change_vector(values: list[float]): # -> list[float]
    retvector = np.array(values) 
