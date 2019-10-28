####
# Первым делом нужно избавится от петель!

n, m = [int(i) for i in input().split()]
edges = [[int(i) for i in input().split()] for _ in range(m)]
vertexes = []
for e in edges:
    if e[0] == e[1]:
        edges.remove(e)
while edges:
    vertexes.append(edges.pop())
    i = 1
    while i >= 0:
        for e in range(len(edges)-1, -1, -1):
            if vertexes[-1][i] in edges[e]:
                v = edges.pop(e)
                v.remove(vertexes[-1][i])
                if v[0] not in vertexes[-1]:
                    vertexes[-1].append(v[0])
                    i = len(vertexes[-1])
                    break
        i -= 1
print(len(vertexes) + n - sum([len(i) for i in vertexes]))

# var 1 can print dictionary

inp = list(map(int, input().split()))
n,m = inp[0], inp[1]

def graph(n, m):
    ribs = list()
    while m > 0:
        ribs.append(list(map(int, input().split())))
        m -= 1
    ribsDict = dict()
    for i in range(n):
        currRibs = []
        for j in range(len(ribs)):
            if ribs[j][0] == i + 1:
                currRibs.append(ribs[j][1])
            elif ribs[j][1] == i + 1:
                currRibs.append(ribs[j][0])
        ribsDict[i + 1] = currRibs
    # print(ribs)
    return ribsDict

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print(graph(n, m))

####





inp = list(map(int, input().split()))
n,m = inp[0], inp[1]

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def graph(n, m):
    ribs = list()
    while m > 0:
        ribs.append(list(map(int, input().split())))
        m -= 1
    ribsDict = dict()
    for i in range(n):
        currRibs = []
        for j in range(len(ribs)):
            if ribs[j][0] == i + 1:
                currRibs.append(ribs[j][1])
            elif ribs[j][1] == i + 1:
                currRibs.append(ribs[j][0])
        ribsDict[i + 1] = currRibs
    print(ribs)
    return ribsDict

print(ToDict(n, m))

###

inp = list(map(int, input().split()))
n,m = inp[0], inp[1]

def ToDict(n, m):
    ribs = list()
    while m > 0:
        ribs.append(inp)
        m -= 1
    ribsDict = dict()
    for i in range(n):
        currRibs = []
        for j in range(len(ribs)):
            if ribs[j][0] == i + 1:
                currRibs.append(ribs[j][1])
            elif ribs[j][1] == i + 1:
                currRibs.append(ribs[j][0])
        ribsDict[i + 1] = currRibs
    # print(ribs)
    return ribsDict

print(ToDict(n, m))

graph = ToDict(n, m)

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    print(visited)
    return visited

# print(dfs(graph, 0))
