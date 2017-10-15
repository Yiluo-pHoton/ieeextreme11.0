from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, v)):
                    return True
            elif parent != i:
                return True
        return False

    def isCyclic(self):
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, -1)) == True:
                    return True
        return False

t = int(input())
for i in range(t):
    n, m = [int(j) for j in input().split()]
    raw = [int(j) for j in input().split()]
    x = raw[0::2]
    fx = raw[1::2]

    g = Graph(n)
    for j in range(m):
        g.addEdge(x[j], fx[j])
    if g.isCyclic():
        print(1)
    else:
        print(0)
