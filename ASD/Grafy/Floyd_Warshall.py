#Floyd_Warshall

#graf podany w postaci macierzowej jeśli nie ma krawędzi to wpisujemy nieskończoność
inf = float("inf")
def Floyd_Warshall(G):
    n = len(G)
    S = G.copy()
    P = [[None for i in range(n)] for j in range(n)]
    for row in range(n):
        for kol in range(n):
            if G[row][kol] != inf:
                P[row][kol] = row
    for i in range(n):
        for x in range(n):
            for y in range(n):
                S[x][y] = min(S[x][y],S[x][i]+S[i][y])
                P[x][y] = P[i][y]
