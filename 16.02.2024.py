#задача 1 
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print(a, " - max", b, " - min")
elif a < b:
    print(b, " - max", a, " - min")
else:
    print("Числа равны")
    
#задача 2
r = int(input("Введите радиус круга: "))
s = int(input("Введите сторону квадрата: "))
r = 2 * r
if r < s :
    print("Впишется")
else:
    print("Не впишется")
    
#задача 3
x = int(input("Введите х: "))
if x < 0:
    print( "y = x **2" )
elif x > 0:
    print("y = 1/(x**2)")
else:
    print("x = 0")
    
#задача 4
k = int(input("Введите радиус круга: "))
l = int(input("Введите сторону квадрата: "))
l = 2 * l
if l > k :
    print("Впишется")
else:
    print("Не впишется")
    
#задача 5
o = int(input("Введите первое число: "))
p = int(input("Введите второе число: "))
if o > p:
    print(o, " - max")
elif o < p:
    print(p, " - max")
else:
    print("Числа равны")
    
