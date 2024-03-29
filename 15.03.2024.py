#coding: utf-8
#задание1

m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10'] 
m.remove(0.25)
m.remove(15)
m.remove("10")
print(m)

#задание 2 
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1:5]
print(abc)

#задание 3
numbers = [1, 4]
numbers.insert(1, 2)
numbers.insert(2, 3)
print(numbers)

#задание 4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass.remove(-6)
mass.remove(-20)
mass.remove(-6)
mass.remove(-4)
mass.sort()
print(mass)
mass.sort(reverse=True)
print(mass)

#задание 5
otr = []
pol = []
nyl = []
i = 0
count = int(input("Введите кол-во чисел: "))
while i < count:
    a = int(input("Введите числа: "))
    i += 1
    if a > 0:
        pol.append(a)
    elif a < 0:
        otr.append(a)
    else:
        nyl.append(a)
otr_summ = 0
pol_summ = 0 
for o in otr:
    otr_summ += o
for p in pol:
    pol_summ += p
print(otr_summ)
if len(pol) == 0:
    print("Нет")
else:
    print(pol_summ / len(pol))
for col in range(len(nyl)):
    nyl[col] = '*'
print(f'Количество звезд: {len(nyl)} {nyl}')

