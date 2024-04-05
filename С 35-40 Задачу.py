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



#Задание 36
import numpy as np
import random

def generate_matrix(M, N):
    return np.random.randint(-9, 10, size=(M, N))

def count_nonzero_elements(matrix):
    return [len(np.where(row != 0)[0]) for row in matrix]

M = 5  # количество строк
N = 4  # количество столбцов

matrix = generate_matrix(M, N)
print("Созданная матрица:")
print(matrix)

nonzero_counts = count_nonzero_elements(matrix)
print("Количество ненулевых элементов в каждой строке:")
print(nonzero_counts)



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



#Задание 38 
import random

def generate_matrix(M, N):
    return [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

def negative_products_array(matrix):
    products = [1] * len(matrix[0])
    for row in matrix:
        for i, val in enumerate(row):
            if val < 0:
                products[i] *= val
    return products

M = 3  # Количество строк в матрице
N = 4  # Количество столбцов в матрице

B = generate_matrix(M, N)
print("Сгенерированная матрица B:\n", B)

negative_products = negative_products_array(B)
print("Одномерный массив произведений отрицательных элементов столбцов:", negative_products)



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
