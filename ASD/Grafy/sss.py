#silnie spójne składowe
# P tablica czasu przetworzenia V tablica czasu wizyty

def DFS(G):
    def DFS_visit(G,s):
        nonlocal time,P,visited
        for vertex in G[s]:
            if not visited[vertex]:
                visited[vertex] = True
                DFS_visit(G,vertex)
        P[time] = s
        time += 1

    n = len(G)
    time = 0
    P = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    for vertex in range(n):
        if not visited[vertex]:
            visited[vertex] = True
            DFS_visit(G,vertex)
    return P

def DFS_2(G,P):
    def DFS_visit(G,s):
        nonlocal time,visited,SKL
        for vertex in G[s]:
            if not visited[vertex]:
                visited[vertex] = True
                DFS_visit(G,vertex)
        SKL[time].append(s)
    n = len(G)
    time = 0
    SKL = []
    visited = [False for _ in range(n)]
    for vertex in range(n-1,-1,-1):
        if not visited[P[vertex]]:
            SKL.append([])
            visited[P[vertex]] = True
            DFS_visit(G,P[vertex])
            time += 1
    return SKL

def sss2(G):
    #tworzymy graf odwrotny
    n = len(G)
    GT = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            GT[G[i][j]].append(i)
    P = DFS(G)
    # print(GT)
    # print(P)
    return DFS_2(GT,P)
# przerabia silnie spójne składowe na graf
def create(G,T):
    n = len(G)
    tab = [-1 for _ in range(n)]
    n2 = len(T)
    for i in range(n2):
        for j in T[i]:
            tab[j] = i
    Graph = [[] for _ in range(n2)]
    for i in range(n):
        for j in G[i]:
            if tab[i] != tab[j] and tab[j] not in Graph[tab[i]]:
                Graph[tab[i]].append(tab[j])
    print(Graph)

G =[[1],[2,4,5],[3,6],[2,7],[0,5],[6],[5,7],[7]]
# create(G,sss(G))
# print(sss2(G))


#Mati


def sss(G):
    n = len(G)
    timeQ = []
    result = []
    visited = [False for _ in range(n)]
    def DFSVisit(G,u):
        nonlocal visited, timeQ
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G,v)
        timeQ.append(u)

    for u in range(n):
        if not visited[u]:
            DFSVisit(G,u)
    
    timeQ = timeQ[::-1]
    revG = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            revG[v].append(u)
    visited2 = [False for _ in range(n)]
    curr = []
    def revDFSvisit(G,u):
        nonlocal curr, visited2
        visited2[u] = True
        for v in G[u]:
            if not visited2[v]:
                revDFSvisit(G,v)
        curr.append(u)

    for u in timeQ:
        curr = []
        if not visited2[u]:
            revDFSvisit(revG,u)
            result.append(curr)
    return result

print(sss(G))
# print(create(G,sss(G)))