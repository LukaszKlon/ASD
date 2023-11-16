def lis(A):
    n = len(A)
    result = [ 1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and result[i] < result[j] + 1:
                result[i] =  result[j]+1
    print(result)

A = [1,2,5,3,6,4,9]
lis(A)

# LIS nlogn


def ceilindex(A,l,r,key):
    while (r-l > 1):
        s = l + (r-l)//2
        if A[s] >= key:
            r = s
        else:
            l = s
    return r
def lis(A):
    n = len(A)
    # result = [ 1 for _ in range(n)]
    s = []
    s.append(A[0])
    for i in range(1,n):
        if A[i] > s[len(s)-1]:
            s.append(A[i])
        else:
            s[ceilindex(A,-1,len(s)-1,A[i])] = A[i]
    return len(s)