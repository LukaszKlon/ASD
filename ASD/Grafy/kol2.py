# Łukasz Klon
# Tworzymy listę krawędzi ((i,j,w) i < j i,j wierzchołki w waga) Algorytm sortuje krawędzie (po długośći trzecia wartość krotki),
#  a następnie wybiera kolejne n-1 krawędzi ( to zapewnia nam że pozostałe krawędzie będą mniejsze lub większe od wszystkich wybranych przez nas)
#  wybieramy krawędzie wpisując true ( w tablicy visited dany wierzchołek został odwiedzony)jeśli wsszystkie zostaały odwiedzone to sprawdzamy
# spójność naszego drzewa jeśli drzewo jest spójne (używamy BFS'a) i każdy wierzchołek został odwieddzony to zwracamy znalezioną sumę jeśli nie wybieramy kolejne n-1 krawędzi i sprawdzamy
# złożoność O(E^2)


from kol2testy import runtests

def edges(G):
    lista = []
    n = len(G)
    for i in range(n):
        for j in G[i]:
            if i < j[0]:
                lista.append((i,j[0],j[1]))
    return lista

from collections import deque

def BFS(G,s):
    Q = deque()
    n = len(G)
    visited = [False for _ in range(n)]
    visited[s] = True
    Q.append(s)
    while len(Q) > 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.append(v)
    for i in range(n):
        if not visited[i]:
            return False
    return True  
def find(edge,s,n):
    visited = [False for _ in range(n)]
    Graph = [[] for _ in range(n)]
    sum = 0
    for i in range(s,s+n-1):
        visited[edge[i][0]] = True
        visited[edge[i][1]] = True
        Graph[edge[i][0]].append(edge[i][1])
        Graph[edge[i][1]].append(edge[i][0])
        sum += edge[i][2]

    for i in range(n):
         if not visited[i]:
              return float("inf")
    if BFS(Graph,0):
        return sum
    return float("inf")

     
def beautree(G):
    n = len(G)
    edge = edges(G)
    edge.sort(key = lambda x : x[2])

    for i in range(len(edge)-n):
        x = find(edge,i,n)
        if x != float("inf"):
            return x
    # return y
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )