import os
os.getwcd()

from decimal import Decimal
a = Decimal("0.5")
b = Decimal("0.4")
print (a-b == Decimal("0.1"))

# Заданы две клетки шахматной доски.
# Если они покрашены в один цвет, то выведите слово YES,
# а если в разные цвета – то NO.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - y1) % 2 == abs(x2 - y2) % 2:
    print("YES")
else:
    print("NO")

# ulitka

from math import ceil
h = float(input())
a = float(input())
b = float(input())
print(ceil((h-a)/(a-b)+1))

## високосный год

a = int(input())
if (((a % 4 == 0) & (a % 100 > 0)) | (a % 400 == 0)):
    print("YES")
else:
    print("NO")


Напишите программу, которая находит сумму чисел в числовом ряду.
Формат входных данных
В первой строке указано количество чисел в числовом ряду, далее сами числа.
Формат выходных данных
Сумма чисел.

import sys
a = list(map(int, sys.stdin.readlines()))
print(sum(a[1:]))

Напишите программу, которая находит сумму чётных чисел в числового ряда.
Формат входных данных
Числовой ряд, заканчивающийся нулём.
Формат выходных данных
Сумма чётных чисел.

import sys
a = list(map(int, sys.stdin.readlines()))
b = []
for i in a:
	if i%2 == 0:
		b.append(i)
print(sum(b))


def count_char(text, char):
	count = 0
	for c in text:
		if c == char:
			count += 1
	return count

a = int(input())
b = int(input())
print(int((a*(a//b) + b*(b//a))/(b//a+a//b)))


c = 0
n = int(input())
#print(n)
for i in range(1,n+1):
    #print(i)
    c += int(input())
print(c)

####

print(sum([int(input()) for i in range(int(input()))]))

####

print(sum(int(input()) for _ in range(int(input()))))

####

# put your python code here
import sys


n = sys.stdin.readline()
data = map(int, sys.stdin.read().split('\n'))
print(sum(data))

a = int(input())
b = int(input())
print('YES'*(((a//b)-(a % b))//(a//b))+'NO'*((((a % b)+2)//((a % b)+1)) % 2))


N = int(input())
h = N // 3600 % 24
if h % 24 == 0:
    h = 0
n = N % 3600
m = n // 60
s = n % 60
sh = str(h)
sm = str(m)
if len(sm) < 2:
    sm = "0" + sm
ss = str(s)
if len(ss) < 2:
    ss = "0" + ss
print(sh, ':', sm, ':', ss, sep='')


hours = N // 60 // 60
min1 = time // 60 % 60 % 10
sek1 = time % 60 % 10
min2 = time // 60 % 60 // 10 % 10
sek2 = time % 60 // 10 % 10
print(hours, ':', min2, min1, ':', sek2, sek1, sep='')


N = int(input())
if N // 60 // 60 <= 23:
    hours = N // 60 // 60
else:
    hours = abs(24 - (N // 60 // 60))

min1 = N // 60 % 60 % 10
sek1 = N % 60 % 10
min2 = N // 60 % 60 // 10 % 10
sek2 = N % 60 // 10 % 10
print(hours, ':', min2, min1, ':', sek2, sek1, sep='')

### Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из моментов времени. Второй момент времени наступил не раньше первого. Определите, сколько часов, минут и секунд прошло между двумя моментами времени.
#Программа на вход получает две строки данных: часы, минуты, секунды разделенные двоеточием, задающие первый и второй моменты времени.
#Выведите число часов, минут и секунд между этими моментами времени в одной строке через пробел.

h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))
t1 = s1 + m1*60 + h1*60*60
t2 = s2 + m2*60 + h2*60*60
o = t2 - t1
print(o // 60 // 60, o // 60 % 60, o % 60)



# TODO: create a function called calculate_diameter that returns the diameter given a circumference
def calculate_diameter(circumference):
  diameter = circumference / 3.14
  return diameter
# TODO: get the circumference from the user
circumference = int(input("Enter circumference:"))
# TODO: call the calculate_diameter function with the user's input and print its result
print(calculate_diameter(circumference))


# TODO: create a function that accepts a radius and calculates and returns the area
def find_area(radius):
  area = 3.14 * (radius**2)
  return area

# TODO: get the radius from the user
radius = int(input("radius:"))
# TODO: call the function above with the user's input and print its result
print(find_area(radius))

# calc

a = float(input())
b = float(input())
x = input()
if x == '+':
  print(a + b)
if x == '-':
  print(a - b)
if x == '/':
  if b == 0:
    print("Деление на 0!")
  else:
    print(a / b)
if x == '*':
  print(a * b)
if x == 'mod':
  if b == 0:
    print("Деление на 0!")
  else:
    print(a % b)
if x == 'pow':
  print(a ** b)
if x == 'div':
  if b == 0:
    print("Деление на 0!")
  else:
    print(a // b)

###

a, b, c = '('+input()+')', input(), input()
d = {'+':'+', '-':'-', '/':'/', '*':'*', 'mod':'%', 'pow':'**', 'div':'//'}
print ('Деление на 0!' if c in 'div/mod' and float(b)==0 else eval(a+d[c]+b))




binary_input = input()
length = len(binary_input)
decimal_value = 0

# here is an example of going through each character in the binary_string
# this does not solve the problem, so you will need to change it
# it just gives you a starting point for your algorithm
for i in range(length):
    decimal_value += int(binary_input[i])*(2**(7-i))
    #print(int(binary_input[i])*(2**(7-i)))

# you need to compute the decimal value and store it in this variable before printing it
print(decimal_value)


#apple
N = int(input())
K = int(input())
print(K//N)

# clock
N = int(input())
print(str(((N // 60) % 24)) + " " + str(N % 60))

#cost
A = int(input())
B = int(input())
N = int(input())
print(str((((A*100+B)*N) // 100)) + " " + str((((A*100+B)*N) % 100)))

# отрезать k цифр с конца
n = int(input())
k = int(input())
print(n // 10 ** k)

# округление вверх
a = int(input())
b = int(input())
print((a + b - 1) // b)

# digits sum
N = int(input())
print(int(str(N)[-1]) + int(str(N)[-2]) + int(str(N)[-3]))

#first digit
N = int(input())
print(str(N)[0])

#last digit
N = int(input())
print(str(N)[-1])

# hello, usr
print('Hello, ' + input() + '!')

# next even
N = int(input())
if N % 2 == 0:
    print(N + 2)
else:
    print(N + 1)

# penguin
n = int(input())
print("   _~_    " * n)
print("  (o o)   " * n)
print(" /  V  \\  " * n)
print("/(  _  )\\ " * n)
print("  ^^ ^^   " * n)

#text
A = int(input())
print("The next number for the number " + str(A) + " is " + str(A + 1) + ".")
print("The previous number for the number " + str(A) + " is " + str(A-1) + ".")

n = int(input())
m = int(input())
if m % n == 0:
    print(m // n)
else:
    print((m // n) + (m % n)**0)

###
