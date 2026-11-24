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
n1 = matrix[:3]; n2 = matrix[-2:]; n3 = matrix[:, -2:]; n4 = matrix[1:4, 2:5]; n5 = matrix[-2:, -2:]

print(n1, n1.shape, n2, n2.shape, n3, n3.shape, n4, n4.shape, n5, n5.shape, sep = '\n')
print()

vector = np.array([10, 20, 30, 40, 50])

vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print(changed_hours, '\n')

##  copy() инициализирует создание отдельного массива для новой переменной,
##  а не просто присваивает новое имя старому, поэтому когда мы вносим изменения,
##  используя новую переменную, видоизменяется не изначальный массив, а новый, созданный

numbers = np.arange(12)
table = numbers.copy().reshape(3, 4)
transposed  = table.copy().T
print(numbers, table, transposed, sep = '\n')

##  для reshape() важно, чтобы кол-во элементов в исходной и желаемой совпадали.
##  в исходной их 12, в матрице 3 на 4 (умножим) также 12, а 5 * 3 = 15.
