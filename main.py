#НОМЕР1
import numpy as np
import random

def generate_matrix_and_find_product(M, N):
    B = np.random.randint(10, size=(M, N))
    positive_elements_product = np.prod(B[B > 0])
    return B, positive_elements_product

M = 3  
N = 4 

B, product = generate_matrix_and_find_product(M, N)

print("Матрица B:")
print(B)
print(f"Произведение положительных элементов: {product}")




#Номер 2
import numpy as np
import random

def generate_matrix_and_find_min(M, N):
    B = np.random.randint(-9, 10, size=(M, N))
    min_value = np.min(B)
    min_row, min_col = np.where(B == min_value)
    return B, min_value, min_row, min_col

M = 3
N = 4

B, min_value, min_row, min_col = generate_matrix_and_find_min(M, N)

print("Матрица B:")
print(B)
print(f"Минимальный элемент: {min_value} расположен в позиции {min_row}, {min_col}")




#Номер 3
import numpy as np
import random

def generate_matrix_and_swap_extremes(M, N):
    D = np.random.randint(-9, 10, size=(M, N))

    min_value = np.min(D)
    max_value = np.max(D)

    min_row, min_col = np.where(D == min_value)
    max_row, max_col = np.where(D == max_value)

    D[min_row, min_col], D[max_row, max_col] = max_value, min_value
    return D

M = 3
N = 4

D = generate_matrix_and_swap_extremes(M, N)

print("Матрица D:")
print(D)




#Номер 4
import numpy as np
import random

def generate_matrix_and_column_products(M, N):
    R = np.random.randint(-9, 10, size=(M, N))
    column_products = np.prod(R, axis=0)
    
    return R, column_products

M = 3
N = 4

R, column_products = generate_matrix_and_column_products(M, N)

print("Матрица Р:")
print(R)
print(f"Одномерный массив произведений элементов каждого столбца: {column_products}")




#Номер 5
import numpy as np
import random
def generate_matrix_and_negative_counts(M, N):
    F = np.random.randint(-9, 10, size=(M, N))
    negative_counts = np.sum(F < 0, axis=1)
    return F, negative_counts

M = 3
N = 4 

F, negative_counts = generate_matrix_and_negative_counts(M, N)

print("Матрица F:")
print(F)
print(f"Одномерный массив количеств отрицательных элементов каждой строки: {negative_counts}")