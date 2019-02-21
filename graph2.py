 k = int(input())
W = []
for i in range(k):
    W.append([(j) for j in input().split()])
minn = 1000
maxx = 0
t = 0
for i in range(k):
    for j in range(k):
            if W[i][j] == 'n' :
                W[i][j] = 30000

def search_min(tr, vizited):
    t = max(tr)
    minn = t

    for ind in vizited:
        for index in enumerate(tr[ind]):
            for elem in enumerate(tr[ind]):
                if elem > 0 and elem < minn and index not in vizited:
                    minn = elem #веса путей
                    index2 = index # индекс города
    return minn, index2

def prim(matr):
    toVisit = [i for i in range(1,5)]# города кроме начального(0)
    vizited = [0]
    result = [0]
    ind = 0
    for index in toVisit:
        weight, ind = search_min(matr, vizited)
        result.append(weight)#в результат будут заноситься веса
        vizited.append(ind)# содержит карту пути
    return result
    print (result)
s = 0
s = prim(W)
print(minn)

Traceback (most recent call last):
  File "C:\Users\Хрюсик\Desktop\Олимпиада\Задача 2.py", line 37, in <module>
    s = prim(W)
  File "C:\Users\Хрюсик\Desktop\Олимпиада\Задача 2.py", line 31, in prim
    weight, ind = search_min(matr, vizited)
  File "C:\Users\Хрюсик\Desktop\Олимпиада\Задача 2.py", line 14, in search_min
    t = max(tr)
TypeError: '>' not supported between instances of 'int' and 'str'
