# BFS

from collections import deque

def BFS(V,s):
    n = len(V)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    len_v = [-1 for _ in range(n)]
    Q = deque()
    len_v[s] = 0
    Q.append(s)
    while len(Q) != 0:
        u = Q.popleft
        for i in range(n):
            if V[u][i] == 1 and not visited[i]:
                len_v[i] = len_v[u] + 1
                parent[i] = u
                visited[i] = True
                Q.append(i)
        q = V[s]
        # while q != None:
        #     i = q.val
        #     if visited[i]:
        #         len_v[i] = len_v[u] + 1
        #         parent[i] = u
        #         visited[i] = True
        #         Q.append(i)
        #     q = q.next
    return visited,parent,len_v

def BFS(G,s):
    Q = deque()
    n = len(G)
    len_ver = [-1 for _ in range(n)]
    parents = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    len_ver[s] = 0
    visited[s] = True
    Q.append(s)
    while len(Q) != 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                len_ver[v] = len_ver[u] + 1
                visited[v] = True
                parents[v] = u
                Q.append(v)
    return len_ver,parents
