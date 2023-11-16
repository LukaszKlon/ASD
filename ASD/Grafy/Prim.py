#Prim Algorithm

from queue import PriorityQueue

# def Prim(G,s):
#     n = len(G)
#     inf = float("inf")
#     P = PriorityQueue()
#     d = [inf for _ in range(n)]
#     d[s] = 0
#     parent = [None for _ in range(n)]
#     P.put((0,s))
#     s = 0
#     while not P.empty():
#         du,u = P.get()
#         # if du > d[u]:
#         #     continue
#         for v,dv in G[u]:
#             if dv < d[v] and parent[u] != v:
#                 s += dv
#                 if d[v] != inf:
#                     s -= d[v]
#                 d[v] = dv
#                 parent[v] = u
#                 P.put((d[v],v))
#             # relax(u,v,dv,d,parent,P)
#     print(d,s)
#     return parent

def Prim(G):
    n = len(G)
    visited = [ False for _ in range(n) ]
    MST = []
    u = 0
    s = 0
    visited[u] = True
    PQ = PriorityQueue()
    
    for count in range(n - 1):
        visited[u] = True
        for v, wuv in G[u]:
            if not visited[v]:
                PQ.put( (wuv, u, v) )
        
        wuv, u, v = PQ.get()
        while visited[v]:
            wuv, u, v = PQ.get()
        
        MST.append( (u, v) )
        s += wuv

        # print(MST)
        # visited[u] = True
        u = v
    
    return MST

G = [
    [(1,5), (6,3), (3,9)],
    [(0,5), (4,8), (2,9)],
    [(1,9), (3,9), (4,4), (7,3)],
    [(0,9), (2,9), (6,8)],
    [(1,8), (2,4), (5,2), (6,1)],
    [(1,6), (4,2), (6,6)],
    [(4,1), (5,6), (2,5), (7,9)],
    [(2,3), (1,7), (6,9)]
]

print(Prim(G))

G = [[(1,1),(4,5),(5,8)],[(0,1),(2,3)],[(1,3),(3,6),(4,4)],[(2,6),(4,2)],[(0,5),(2,4),(3,2),(5,7)],[(0,8),(4,7)]]
# G2 = [[(3, 12), (2, 8)], [(3, 4), (6, 5)], [(4, 9), (0, 8)], [(0, 12), (1, 4)], [(5, 8), (2, 9)], [(6, 2), (4, 8)], [(1, 5), (5, 2)]]
# print(Prim(G2))
