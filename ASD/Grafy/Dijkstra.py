from queue import PriorityQueue
from math import inf
def relax(u,v,l,d,parent,P):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
        P.put((d[v],v))

def Dijkstra(G,s):
    n = len(G)
    inf = float("inf")
    P = PriorityQueue()
    d = [inf for _ in range(n)]
    d[s] = 0
    parent = [None for _ in range(n)]
    P.put((0,s))
    while not P.empty():
        du,u = P.get()
        if du > d[u]:
            continue
        for v,dv in G[u]:
            relax(u,v,dv,d,parent,P)
    return d

def relax(u,v,l,d,parent,P):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
        P.put((d[v],v))

def Dijkstra(G,s):
    n = len(G)
    P = PriorityQueue()
    d = [inf for _ in range(n)]
    d[s] = 0
    parent = [None for _ in range(n)]
    P.put((0,s))
    while not P.empty():
        du,u = P.get()
        if du == d[u]:
            for v,dv in G[u]:
                relax(u,v,dv,d,parent,P)
    return d
G = [[(1,1),(2,2)],[(0,1),(3,3),(4,3)],[(0,2),(3,1),(7,7)],[(1,3),(2,1),(5,2),(8,3)],[(1,3),(5,5)],[(3,2),(4,5),(6,1)],[(5,1),(7,4),(8,8)],[(2,7),(6,4),(8,1)],[(3,3),(6,8),(7,1)]]
# G2=[[-1,1,2,-1,-1,-1,-1,-1,-1],
#     [1,-1,-1,3,3,-1,-1,-1,-1],
#     [2,-1,-1,1,-1,-1,-1,7,-1],
#     [-1,3,1,-1,-1,2,-1,-1,3],
#     [-1,3,-1,-1,-1,5,-1,-1,-1],
#     [-1,-1,-1,2,5,-1,1,-1,-1],
#     [-1,-1,-1,-1,-1,1,-1,4,8],
#     [-1,-1,7,-1,-1,-1,4,-1,1],
#     [-1,-1,-1,3,-1,-1,8,1,-1]
#     ]
# for i in range(len(G2)):
#     for j in range(len(G2)):
#         if G2[i][j] != -1:
#             print((j,G2[i][j]),end=",")
#     print("")
def Dijkstra_m(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    for _ in range(n):
        u = -1
        cur_dist = inf
        for i in range(n):
            if not visited[i] and d[i] < cur_dist:
                u = i
                cur_dist = d[i]
        if u == -1:
            break
        for i in range(n):
            if G[u][i] != -1 and d[i] > d[u] + G[u][i]:
                parent[i] = u
                d[i] = d[u] + G[u][i]
        visited[u] = True
    return d
        

print(Dijkstra(G,0))        
# print(Dijkstra_m(G2,0))



