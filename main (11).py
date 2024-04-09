#coding: utf-8 
#Задание 35 
import random 

def generate_matrix():
    matrix = [[random.randint(-10, 10) for _ in range(4)] for _ in range(7)]
    return matrix

def sum_positive_elements(matrix):
    positive_sums = [sum(row) for row in matrix if any(row)]
    return positive_sums

matrix = generate_matrix()
print(matrix)


positive_sums = sum_positive_elements(matrix)
print(positive_sums)



#Задание 37 
import random

def generate_matrix(M, N):
    return [[random.randint(0, 1) for _ in range(N)] for _ in range(M)]

def count_nonzero_elements(matrix):
    return [sum(1 for element in row if element) for row in matrix]

M = 3  # Количество строк в матрице
N = 4  # Количество столбцов в матрице

A = generate_matrix(M, N)
print("Сгенерированная матрица A:\n", A)

nonzero_counts = count_nonzero_elements(A)
print("Одномерный массив количеств ненулевых элементов строк матрицы:", nonzero_counts)


#Задание 39 
import random

def generate_matrix(M, N):
    return [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

def min_elements_array(matrix):
    return [min(row) for row in matrix]

M = 3  # Количество строк в матрице
N = 4  # Количество столбцов в матрице

A = generate_matrix(M, N)
print("Сгенерированная матрица A:\n", A)

min_elements = min_elements_array(A)
print( min_elements)



#Задача 40 
import random

def generate_matrix(M, N):
    return [[random.randint(0, 1) for _ in range(N)] for _ in range(M)]

def count_nonzero_elements(matrix):
    return [len([item for item in row if item != 0]) for row in matrix]

M = 3  # Количество строк в матрице
N = 4  # Количество столбцов в матрице

A = generate_matrix(M, N)
print("Сгенерированная матрица A:\n", A)

nonzero_counts = count_nonzero_elements(A)
print("Одномерный массив количеств ненулевых элементов строк матрицы:", nonzero_counts)

# Задание 43
stolbi = 5
stroki = 3
B = []
nulevoy_spisok = []
Ne_nulevoy_spisok = []
for stolb in range(stolbi):
    nulevoy_el = 0
    Ne_nulevoy_el = 0
    matrix_numb = []
    for stroka in range(stroki):
        matrix_numb.append(random.randint(-5, 5))
    B.append(matrix_numb)
    for i in matrix_numb:
        if i == 0:
            nulevoy_el += 1 
            continue
        elif i != 0:
            Ne_nulevoy_el += 1
    nulevoy_spisok.append(nulevoy_el)
    Ne_nulevoy_spisok.append(Ne_nulevoy_el)
    # nulevoy_spisok.append(matrix_numb.count(0))

for vivod in B:
    print(vivod)
print('\n', 'Количество нулевых элементов', nulevoy_spisok)
print('\n', 'Количество ненулевых элементов', Ne_nulevoy_spisok)