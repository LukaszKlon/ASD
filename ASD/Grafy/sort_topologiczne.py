
def top_sort(G):
    n = len(G)
    def DFSvisit(G,u):
        nonlocal visited,sort,inp
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                DFSvisit(G,v)
                sort[inp] = v
                inp -= 1
    visited = [False for _ in range(n)]
    sort = [-1 for _ in range(n)]
    time = 0
    inp = n-1
    for v in range(n):
        if not visited[v]:
            DFSvisit(G,v)
            sort[inp] = v
    return sort

# O(E+V)

G=[[1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]]
print(top_sort(G))
        