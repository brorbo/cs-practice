import numpy as np

table = np.array([[18, 20, 19, 21],
                  [17, 18, 20, 22],
                  [16, 19, 21, 23]])
print(table.shape)       # (3, 4): три строки, четыре столбца
print(table[1])          # строка с индексом 1
print(table[:, 3])       # столбец с индексом 3
print(table[:2, 1:3])    # первые две строки, столбцы 1 и 2

hours = np.array(range(0, 22, 3))
line = np.array([0, 0.25, 0.5, 0,75, 1])
zeros = np.array([0]*6)
unknown_table = np.array([[-1]*2]*3)
identity = np.array([[1]*3]*3)


print(hours, hours.shape, hours.ndim, hours.size, hours.dtype, sep = '\n')
print()
print(hours[2], hours[-1], hours[2:6], hours[::2], hours[::-1], sep = '\n')
print()

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape, temperatures.size, temperatures[1][2], temperatures[0], temperatures[:, -1], \
      temperatures[:2, 1:], temperatures[:2, 1:3], sep = '\n')
print()

matrix = np.arange(1, 26).reshape(5, 5)

