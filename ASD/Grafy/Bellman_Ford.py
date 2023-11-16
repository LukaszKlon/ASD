
def relax(u,v,l,d,parent):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
    

def Bellman_Ford(G,s):
    n = len(G)
    inf = float("inf")
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    for i in range(n-1):
        for u in range(n):
            for v,dv in G[u]:
                relax(u,v,dv,d,parent)
    for u in range(n):
        for v,dv in G[u]:
            if d[v] > d[u] + dv:
                return False
    return d
    
G = [[(1,1),(2,2)],[(0,1),(3,3),(4,3)],[(0,2),(3,1),(7,7)],[(1,3),(2,1),(5,2),(8,3)],[(1,3),(5,5)],[(3,2),(4,5),(6,1)],[(5,1),(7,4),(8,8)],[(2,7),(6,4),(8,6)],[(3,3),(6,8),(7,1)]]

print(Bellman_Ford(G,0))