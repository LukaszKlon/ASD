
class Find_Union():
    def __init__(self,v):
        self.parents = [x for x in range(v)]
        self.rank = [0 for _ in range(v)]
    
    def find_root(self,x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find_root(self.parents[x])
        return self.parents[x]
    
    def Union(self,x,y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)
        if self.rank[root_x] > self.rank[root_y]:
            self.parents[root_y] = root_x
        else:
            self.parents[root_x]= root_y
            if self.rank[root_x]==self.rank[root_y]:
                self.rank[root_y] += 1


def edges(G):
    lista = []
    n = len(G)
    for i in range(n):
        for j in G[i]:
            if i < j[0]:
                lista.append((i,j[0],j[1]))
    return lista


def Kruskal(G):
    lista = edges(G)
    A = []
    lista.sort(key = lambda x:x[2])
    FU = Find_Union(len(G))
    sum = 0
    for u,v,w in lista:
        v1 = FU.find_root(u)
        v2 = FU.find_root(v)
        if v1 != v2:
            sum += w
            A.append((u,v,w))
            FU.Union(u,v)
    return sum    

    #miasta połączono siecią autostrad współrzędne miasta x,y kruskal budowany n razy 