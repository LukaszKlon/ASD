s1 = input()
s2 = input()
n = len(s1)
m = len(s2)
T = [[0 for _ in range(n+1)] for _ in range(m+1)]
x = 1
result = ''
for i in range(1,m+1):
   for j in range(1,n+1):
       if s1[j-1] == s2[i-1]:
           T[i][j] = T[i-1][j-1] +1 
       else:
           T[i][j] = max(T[i-1][j],T[i][j-1])
i = m
j = n
while T[i][j] != 0:
    while T[i][j] == T[i-1][j]:
        i -= 1
    while T[i][j] == T[i][j-1]:
        j -= 1
    result += s1[j-1]
    i -= 1
    j -= 1
print(T[m][n])
print(result[::-1])