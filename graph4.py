inp =list(map(int,input().split()))

n,m = inp[0],inp[1]

n, m = map(int, input().split())

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
