import numpy as np

def create_array(d1, d2, d3, val):
    return np.full((d1, d2, d3), val)

arr = create_array(3, 4, 5, 6)
print(arr)
