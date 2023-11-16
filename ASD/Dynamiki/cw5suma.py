
def sum(A,T):
    n = len(A)
    DP = [[False for _ in range(n)] for _ in range(T+1)]
    DP[0][0] = True
    DP[A[0]][0] = True
    for i in range(1,n):
        for j in range(T+1):
            DP[j][i] = DP[j][i-1]
            if j - A[i] >= 0:
                DP[j][i] = DP[j][i] or DP[j-A[i]][i]
    for i in DP:
        print(i)

T = [1,4,2,2,3]
s = 7
sum(T,s)
        