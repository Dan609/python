def dfs(v):  # dfs is an acronym for "depth-first search"
    for w in adj_list[v]:  # переменная w пробегает всех соседей вершины v
        dfs(w)

dfs(s)
