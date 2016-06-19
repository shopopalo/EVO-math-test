import operator
import random

# создание матрицы с помощью циклов
matrix = []
for i in range(10):
	matrix.append([])
	for j in range(10):
		matrix[i].append([])
		for num in range(10):
			matrix[i][j].append(random.randint(0,9))

# создание матрицы с помощью List comprehensions
#matrix = [[[random.randint(0,9) for z in range(10)] for j in range(10)] for i in range(10)]


# словарь для хранения сумм элеметов по столбцам
summ_columns_dict = {}
# ключ словаря summ_columns_dict
number_column = 0
for two in range(len(matrix[0][0])):
	for three in range(len(matrix[0])):
		# сумма элементов столбца
		summ_elements = 0
		for one in range(len(matrix)):
			summ_elements += matrix[one][two][three]
		summ_columns_dict[number_column] = summ_elements
		number_column += 1

sorted_res_dict = sorted(summ_columns_dict.items(), key=operator.itemgetter(1))
# вывод отсортированого словаря (столбец, сумма)
#print(sorted_res_dict)

# три столбца с максимальной суммой
# (столбец, сумма)
print(sorted_res_dict[-3:])

# вывод матрицы
#for line in matrix:
#	print(line)