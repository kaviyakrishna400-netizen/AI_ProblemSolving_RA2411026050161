graph = {
'A':['B','C'],
'B':['A','D'],
'C':['A','E'],
'D':['B','F'],
'E':['C','F'],
'F':[]
}

visited=[]

def bfs(start,goal):
    queue=[[start]]

    while queue:
        path=queue.pop(0)
        node=path[-1]

        if node==goal:
            print("BFS Path:", path)
            return

        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                new_path=list(path)
                new_path.append(neighbor)
                queue.append(new_path)

bfs('A','F')
