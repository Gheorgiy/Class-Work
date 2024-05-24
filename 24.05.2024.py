#coding: utf-8
#задача # 1 
def sum(start, end):
    if start > end:
        return sum(start, end)
    total = 0
    while start <= end:
        total += start
        start += 1 
print(sum(4, 2)) 
print(sum(4, 2))


def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))

# Тесты
print(sum_range(1, 5))  # 15
print(sum_range(5, 1))  # 15
print(sum_range(-3, 4))  # 4
