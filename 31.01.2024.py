    #задача 11 
v = int(input("Объем: "))
m = int(input("Масса: "))
p = m * v 
print("Ответ: ", p )

    #Задача 12
x = int(input("Введите число 1: "))
y = int(input("Введите число 2: "))
l = x + y
s = x - y 
e = x * y 
f = x / y 
print("Ответ сложения: ", l )
print("Ответ вычитание: ", s )
print("Ответ умножения: ", e )
print("Ответ деления: ", f )

    #Задача 13
x1 = int(input("Введите число 1: "))
y1 = int(input("Введите число 2: "))
h = (x1 + y1 / 2)
sprt = (x1 * y1)
print("Среднее арифметическое знач: ", h )
print("Среднее геометрическое знач: ", sprt )

    #Задача 14 
x2 = int(input("Площадь государства: "))
y2 = int(input("Кол-во жителей: "))
h1 = (y2 / x2)
print("Ответ: ", h1)

    #Задача 15 
x3 = int(input("Ребро паралл1: "))
y3 = int(input("Ребро паралл2: "))
y4 = int(input("Ребро паралл3: "))
h2 = 2 * (x3 * y3 + x3 * y4 + y4) #формула вычисления площади полной поверхности 
f1 = x3 * y3 * y4 #формула вычисления объема параллелепипеда 
print("Площадь п.п: ", h2 )
print("Объем: ", f1 )