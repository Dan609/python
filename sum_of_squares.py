#!/usr/bin/env python
# -*- coding: utf-8 -*-

sum = 0
b = [0]
while True:
    a = int(input())
    sum += a
    d = b.append(a)
    if sum == 0:
        break
for i in b:
    sum += i*i
print(sum)

'''
Напишите программу, которая считывает числа по одному в строке до тех пор,
пока сумма введённых чисел не будет равна 0
и сразу после этого выводит сумму квадратов всех считанных чисел.
'''

s=[int(input())]
while sum(s)!=0: s.append(int(input()))
print(sum([i**2 for i in s]))

# чудесное свойство функции print. Пример:

L = [1, 2, 3, 4, 5]
print(*L) #функция просто выведет все элементы списка через пробел
