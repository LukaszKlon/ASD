
def Bridges(G):
    
    def DFSvisit(G,u):
        nonlocal time,visited,parent,times,bridges
        time += 1
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                times[v] = time
                DFSvisit(G,v)
        Flag = True
        for v in G[u]:
            if times[u] > times[v] and v != parent[u]:
                times[u] = times[v]
                Flag = False
        if Flag and parent[u] != None:
            bridges.append((parent[u],u))

    n = len(G)
    time = 1
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    times = [0 for _ in range(n)] 
    bridges = []
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            times[i] = time
            DFSvisit(G,i)
    DFSvisit(G,0)
    print(times)
    print(bridges)
    return bridges

G = [[1,2],[0,2,4],[0,1],[4,5],[1,3,5],[3,4]]
G2 = [[1,4],[0,2,4],[1,3,4],[2,5,6],[0,1],[3,6,7],[3,5,7,10],[5,8,9],[7],[7],[6,11,12,13],[10,12,13],[10,11,13],[10,11,12]]
print(Bridges(G2))

