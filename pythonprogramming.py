inp =list(map(int,input().split()))
n,m = inp[0],inp[1]

n, m = map(int, input().split())

adj = [[0]*n for _ in range(n)]

for it in range(m):
    r, c = map(int, input().split())
    adj[r-1][c-1] = adj[c-1][r-1] = 1

print(adj)

ex = set()       # множество посещенных вершин
def dfs(node):   # start - начальная вершина
    ex.add(node)
    for enotik in range(len(garage)):
        if garage[node][enotik] == 1 and enotik not in ex:
            print(enotik)
            dfs(enotik)
