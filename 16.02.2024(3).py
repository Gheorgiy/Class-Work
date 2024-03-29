#coding: utf-8
a = int(input("Введите количсевто чисел ряда Фибоначчи: "))
fib1 = 0
fib2 = 1
print(fib1)
print(fib2)
i = 2
while i < a:
    s = fib1 + fib2
    print(s)
    fib1 = fib2
    fib2 = s
    i += 1
