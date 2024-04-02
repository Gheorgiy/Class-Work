#Задача 1 
def schet ():
    a = input ("Введите первое число: ")
    a = float (a)
    b = input ("Введите второе число: ")
    b = float (b)
    c = input ("Введите третье число ")
    c = float (c)
    if a > b: 
        print(a - b)
    else: 
        print(b - a)
    return a, b
    
    if b > c:
        print(b - c)
    else:
        print(c - b)
    return c, b 
    
c, d = schet ()
e, f = schet ()
z, x = schet ()

#Задача 2
def schet1 ():
    a = input ("Введите первое число: ")
    a = float (a)
    b = input ("Введите второе число: ")
    b = float (b)
    c = input ("Введите третье число ")
    c = float (c)
    if a > b: 
        print(a - b)
    else: 
        print(b - a)
    return a, b
    
    if b > c:
        print(b + c)
    else:
        print(c + b)
    return c, b 
    
c, d = schet1 ()
e, f = schet1 ()
z, x = schet1 ()

#Задача 3
def swed ():
    a = input("Висит груша нельзя скушать - это? ")
    a2 = input("Два кольца, два конца, посредине - Дружба. Что это? ")
    a3 = input("Висит коса, не косится трава. Люди её не согнут, а она сама гнётся. Что это? ")
    if a == "лампочка":
        print("Правильно!")
    else:
        print("Неправильно.")
        
    if a2 == "ножницы":
        print("Правильно!")
    else:
        print("Неправильно.")
        
    if a3 == "барометр":
        print("Правильно!")
    else:
        print("Неправильно.")

c, d = swed ()
e, f = swed ()
z, x = swed ()
