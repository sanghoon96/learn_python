data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = data * 2
print(result, type(result))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

import numpy as np

x = np.array(data)
print(x, type(x))
# (array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), numpy.ndarray)
result = x + 2
print(result, type(result))
# (array([ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), numpy.ndarray)
x * 2, x // 2
# (array([ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]),
# array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4]))
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
result = 2 * a + b
print(result, type(result), result.ndim)
# (array([12, 24, 36]), numpy.ndarray, 1)