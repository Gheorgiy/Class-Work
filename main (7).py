print("22.03  С ДНЕМ РОЖДЕНИЯ ♡♡♡♡♡♡♡")

#Задача 1 

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
if a > b:
    print(a, " - max", b, " - min")
elif a < b:
    print(b, " - max", a, " - min")
else:
    print("Числа равны")

#Задача 2 

a1 = int(input("Введите число для 1 стороны "))
a2 = int(input("Введите число для 2 стороны "))
a3 = int(input("Введите число для 3 стороны "))
if ( a1 + a2 ) >= a3:
    print("YES")
elif(a1 + a3 ) >= a2:
    print("YES")
elif (a2 + a3 ) >= a1:
    print("YES")
else:
    print("NO")

#Задача 3 

donnmee = int(input("Введите число "))
if ( donnmee % 4 == 0 and donnmee % 100 != 0 ) or donnmee % 400 == 0:
    print("YES")
else:
    print("NO")