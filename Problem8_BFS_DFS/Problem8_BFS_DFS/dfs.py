graph = {
'A':['B','C'],
'B':['A','D'],
'C':['A','E'],
'D':['B','F'],
'E':['C','F'],
'F':[]
}

visited=set()

def dfs(node,goal,path):
    path.append(node)

    if node==goal:
        print("DFS Path:",path)
        return True

    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor,goal,path):
                return True

    path.pop()
    return False

dfs('A','F',[])
