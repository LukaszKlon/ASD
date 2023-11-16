
def DFS(G):
    def DFSvisit(G,u):
        nonlocal time,visited,parent
        time += 1
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                visited[v] = True
                DFSvisit(G,v)
        time +=1

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    time = 0
    for v in range(n):
        if not visited[v]:
            DFSvisit(G,v)
    