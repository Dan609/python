inp =list(map(int,input().split()))
n,m = inp[0],inp[1]



n, m = map(int, input().split())
adj = [[0]*n for _ in range(n)]

for it in range(m):
    r, c = map(int, input().split())
    adj[r-1][c-1] = adj[c-1][r-1] = 1

print(adj)



import numpy as np
a = [5,1,2,2]
b = [3,3,3,5]
m = np.zeros((6,6))
m[a, b] = 1
m[b, a] = 1



# 1. Матрица связности.
garage = [[0,1,0],  # матрица связности
     [1,0,0],
     [0,0,0]]

ex = set()       # множество посещенных вершин
def dfs(node):   # start - начальная вершина
    ex.add(node)
    for enotik in range(len(garage)):
        if garage[node][enotik] == 1 and enotik not in ex:
            print(enotik)
            dfs(enotik)

# 2. Список смежности.
list_of_enotiki = [[1,3], [0], [3], [2,0], []]
vladimir = [False for enotu in range(len(list_of_enotiki ))]

def dfs(vovan):
    vladimir[vovan] = True
    for vovochka in list_of_enotiki[vovan]:
        if not vladimir[vovochka]:
            dfs(vovochka)

for cotiki in range(len(list_of_enotiki)):
    if not vladimir[cotiki]:
        dfs(cotiki)
