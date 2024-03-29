#coding: utf-8
#задача 15
import random
size = int(input("Введите размерность массива: "))
array = [random.randint(-100, 100) for _ in range(size)]
squared_array = [n ** 2 for n in array]
cubed_array = [n ** 3 for n in array]
print("Квадраты элементов массива:", squared_array)
print("Кубы элементов массива:", cubed_array)

#задача 16
a, b, c = map(int, input("Введите три числа, разделенные пробелами: ").split())
print("Наименьшее число:", min(a, b, c))

#задача 17
char = input("Введите символ: ")
num = int(input("Введите целое число: "))

print("Остаток от деления кода символа на число:", chr(num % ord(char)))

#задача 18
char = input("Введите символ: ")
num = float(input("Введите вещественное число: "))

print("Целая часть от деления числа на код символа:", num // ord(char))

#задача 19
def find_area(x1, y1, x2, y2, x3, y3):
    a = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
    return abs(a)

x1 = float(input("Введите координату x для первой вершины: "))
y1 = float(input("Введите координату y для первой вершины: "))
x2 = float(input("Введите координату x для второй вершины: "))
y2 = float(input("Введите координату y для второй вершины: "))
x3 = float(input("Введите координату x для третьей вершины: "))
y3 = float(input("Введите координату y для третьей вершины: "))

print("Площадь треугольника:", find_area(x1, y1, x2, y2, x3, y3))



