
time = 0
def dfs(G,art,low,d,parent,v):
    global time
    children = 0
    time += 1
    low[v] = time
    d[v] = time

    for u in G[v]:
        if d[u] is None:
            children += 1
            dfs(G,art,low,d,parent,u)

            if low[u] >= d[v]:
                art[v] = True
            low[v] = min(low[u],low[v])
        else:
            low[v] = min(low[v],d[u])
    return children  

def articulation(G):
    n = len(G)
    low = [0 for _ in range(n)]
    art = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [None for _ in range(n)]

    for i in range(n):
        if d[i] == None:
            if dfs(G,art,low,d,parent,i) > 1:
                art[i] = True
            else:
                art[i] = False
    print(art)

    

G = [[1,2,3],[0,2],[0,1],[0,4,5],[3,5],[3,4]]
print(articulation(G))
            
    
