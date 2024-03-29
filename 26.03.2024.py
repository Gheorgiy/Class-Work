#coding: utf-8
#задача 27

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
arr2 = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
arr3 = arr1 + arr2
arr3 = list(set(arr3))
print(arr3)

#задача 28

B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(B)
count_nonzero = sum(map(lambda x: x.count(0), B))
print(f"Количество ненулевых элементов: {count_nonzero}")


#задача 29 

D = [[1, 2, 3], [4, -5, 6], [7, 8, 9]]
print(D)
negative_elements_product = 1
for row in D:
    for element in row:
        if element < 0:
            negative_elements_product *= element

print(f"Произведение отрицательных элементов: {negative_elements_product}")

#задача 30 

B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(B)
positive_elements_product = 1
for row in B:
    for element in row:
        if element > 0:
            positive_elements_product *= element

print(f"Произведение положительных элементов: {positive_elements_product}")

#задача 31

B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(B)
min_element = min(B)
min_coords = B.index(min_element)
print(f"Минимальный элемент: {min_element}")
print(f"Координаты минимального элемента: {min_coords}")
