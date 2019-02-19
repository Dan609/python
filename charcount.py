s = input() + "0"
c = 1
i = 0
j = 1
p = []
if len(s) == 2:
  print(s[0] + "1")
else:
  while j != len(s):
      p.append(s[i])
      while s[i] == s[j]:
        j += 1
        c += 1
      p.append(c)
      i += c
      j = i + 1
      c = 1
print(''.join(str(x) for x in p))


###

genome = input()+' '
s = 0
n=genome[0]
for i in genome:
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1

###

a=input()
s=1
a=a+'0'
for j in range (0,len(a)-1):
    if a[j]==a[j+1]:
     s+=1
    else:
     print((a[j]+str(s)),end='')
     s=1

###

dna = input()                    # считываем строку
print(dna[0],end='')             # выводим первый символ
cnt = 1                          # счетчик символов на единице
for i in range(0,len(dna)-1):    # итератор проходит по всем индексам символов кроме предпоследнего
    if dna[i] == dna[i+1]:       # сравниваем символ по текущему индексу со следующим
        cnt+=1                   # если символы одинаковые, то увеличиваем счетчик
    else :
        print(cnt,end='')        # если разные, то выводим значение счетчика
        print(dna[i+1],end='')   # выводим следующий символ
        cnt = 1                  # счетчик текущего символа на единице
print(cnt)                       # в конце распечатываем значение счетчика последнего символа

###

s,n = 0,input()+' '
for i in n:
    if n[0] != i:
        print(n[0],s,end='',sep='')
        s,n = 0,i
    s += 1

###

a = input()+' '
count = 1
for i in range(len(a)-1):
	if a[i] != a[i + 1]:
		print(a[i] + str(count), end='')
		count = 1
	else:
		count += 1

###

import itertools
print("".join([k+str(len(list(g))) for k, g in itertools.groupby(input())]))

###

from itertools import groupby

print(''.join(f'{char}{len(list(group))}' for char, group in groupby(input())))

###

s = input() + ' '    #исходный список, закрываем пробелом
ind = 0
for i in range(1, len(s)):    #будем проходится по индексам, начиная с 1
    if s[i] != s[i-1]:    #находим несовпадение, начинаем работать, иначе проходим дальше
        print(s[i-1] + str(i - ind), end='')    #записываем предыдущий символ и (текущий индекс минус предыдущий)=кол-во
        ind = i    #сохраняем текущий индекс для следующей итерации

###
