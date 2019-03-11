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
