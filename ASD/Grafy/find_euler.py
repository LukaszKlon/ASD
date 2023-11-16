
def find_euler(G):
    n = len(G)
    edges = [[False for _ in range(n)] for i in range(n)]
    cycle = []
    def DFSvisit(G,u):
        nonlocal cycle,edges
        for v in G[u]:
            if not edges[u][v]:
                edges[u][v] = True
                edges[v][u] = True
                DFSvisit(G,v)
        cycle.append(u)
    DFSvisit(G,0)
    return cycle

G = [
    [1,2],
    [0, 2, 3, 4, 6],
    [0, 1, 3, 5, 6],
    [1, 2, 4, 5],
    [1, 2, 3, 5],
    [1, 2, 3, 4],
    [1, 2]
]
print(find_euler(G))
