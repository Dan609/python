graph = {'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']}

def dfs(s,d):

  def dfs_helper(s,d):
       if s == d:
           return True
       if  s in visited :
           return False
       visited.add(s)
       for c in graph[s]:
           dfs_helper(c,d)
       return False
   visited = set()
   return dfs_helper(s,d)
