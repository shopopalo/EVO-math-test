import random
import operator

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
summ_columns_dict_i = {}
# ключ словаря summ_columns_dict_i
number_column_i = 0
for two in range(len(matrix[0][0])):
	for three in range(len(matrix[0])):
		# сумма элементов столбца
		summ_elements = 0
		for one in range(len(matrix)):
			summ_elements += matrix[one][two][three]
		summ_columns_dict_i['i'+str(number_column_i)] = summ_elements
		number_column_i += 1

# вывод матрицы
#for line in matrix:
#	print(line)

summ_columns_dict_i = sorted(summ_columns_dict_i.items(), key=operator.itemgetter(1))
print(summ_columns_dict_i[-1])

# словарь для хранения сумм элеметов по столбцам
summ_columns_dict_j = {}
# ключ словаря summ_columns_dict_j
number_column_j = 0
for i in range(len(matrix)):
	#print(matrix[i])
	for j in range(len(matrix[0])):
		#print(matrix[i][j])
		summ_columns_dict_j['j'+str(number_column_j)] = sum(matrix[i][j])
		number_column_j += 1

summ_columns_dict_j = sorted(summ_columns_dict_j.items(), key=operator.itemgetter(1))
print(summ_columns_dict_j[-1])


