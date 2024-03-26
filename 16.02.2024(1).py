#задача 1 
a = int(input("Введите число: "))
if a > 0:
    print(a, "это число больше 0")
elif a == 0:
    print(a, "А это число равно 0")
else: 
    print(a, "Ну это меньше 0 чел")

#задача 2 
b = int(input("Введите любое число ^-^  "))
if b > 0:
    print("1")
else:
    print("-1")
    
#задача 3
print("Хотите погладить котика? {Да, Нет}")
c = input()
if c == 'Да':
    print("Сколько хотите погладить раз?")
    d = int(input())
    print("Вы погладили котика ", d , " раз. Котик доволен ^-^")
elif c == 'Нет': 
    print("Котик хочет, чтобы его погладили :(  ")
else:
    print("Надо отвечать только Да или Нет")
    
#задача 4
f = int(input("Введите первое число: "))
h = int(input("Ведите второе число: "))
if f > h:
    k = print(f - h)
elif f < h:
    k = print(f + h)
else:
    k = f
    print(k)

#задача 5
print("Угадайте, какое число я загадал от 1 до 10)  ")
l = int(input())
while l <= 10:
    if l == 5:
        print("Да, верно")
        break
    elif l == 7: 
        print("неверно")
        break
    elif l == 1:
        print("Неверно")
        break
    elif l == 3:
        print("Неверно")
        break
    elif l == 4:
        print("Неверно")
        break
else:
    print("Это число не входит в диапозон")
    
    
    
