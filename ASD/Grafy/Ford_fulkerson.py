from collections import deque

def BFS(G,s):
    Q = deque()
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    len_v = [0 for _ in range(n)]
    visited[s] = True
    Q.append(s)
    while len(Q) >0:
        x = Q.popleft()
        for i in range(n):
            if G[x][i] > 0  and not visited[i]:
                len_v[i] =len_v[x] + 1
                parent[i] = x
                visited[i] = True
                Q.append(i)
    return parent

def min_weight(G,Parent,t):
    min = float("inf")
    i = t
    while Parent[i] != None:
        if G[Parent[i]][i] < min:
            min = G[Parent[i]][i]
        i = Parent[i]
    return min

def update_weights(G,Parent,t,min):
    i = t
    while Parent[i] != None:
        G[Parent[i]][i] -= min
        G[i][Parent[i]] += min
        i = Parent[i]
    return min    

from copy import deepcopy
def Ford_Fulkerson(G,s,t):
    n = len(G)
    G2 = deepcopy(G)
    path = BFS(G,s)
    count_flows = 0
    while path[t] != None:
        min = min_weight(G,path,t)
        count_flows += min
        update_weights(G,path,t,min)
        path = BFS(G,s)
    return count_flows

G = [[0,1000,1000,0],[0,0,0,1000],[0,1,0,1000],[0,0,0,0]]
print(Ford_Fulkerson(G,0,3))


# Listowy
def DFS(G,s,t):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    stack = deque()
    stack.append(s)
    visited[s] = True
    while len(stack) > 0:
        u = stack.pop()
        for v in G[u][::-1]:
            if not visited[v]:
                parent[v] = u
                visited[v] = True
                stack.append(v)
        if visited[t]:
            return parent
    return parent
        

def update_edges(G,Parent,t):
    i = t
    while Parent[i] != None:
        G[i].append(Parent[i])
        G[Parent[i]].remove(i)
        i = Parent[i]    

def Ford_Fulkerson(G,s,t):
    n = len(G)
    path = DFS(G,s,t)
    count_flows = 0
    while path[t] != None:
        count_flows += 1  
        update_edges(G,path,t)
        path = DFS(G,s,t)
    return count_flows