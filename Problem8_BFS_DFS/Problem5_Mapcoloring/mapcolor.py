colors = ["Red","Green","Blue"]

graph = {
'A':['B','C'],
'B':['A','C','D'],
'C':['A','B','D'],
'D':['B','C']
}

assigned = {}

def safe(node,color):
    for neighbor in graph[node]:
        if neighbor in assigned and assigned[neighbor]==color:
            return False
    return True

def solve():
    for node in graph:
        for color in colors:
            if safe(node,color):
                assigned[node]=color
                break

    print(assigned)

solve()
