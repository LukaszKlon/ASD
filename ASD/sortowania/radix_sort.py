def counting_sort_radix(T,index):
    n = len(T)
    k = 26
    TMP = [0 for _ in range(k)]
    T2 = [0 for _ in range(n)]
    for i in T:
        TMP[ord(i[index])-97] += 1
    for i in range(1,k):
        TMP[i] += TMP[i-1]
    for i in range(n-1,-1,-1):
        T2[TMP[ord(T[i][index])-97]-1] = T[i]
        TMP[ord(T[i][index])-97] -= 1
    return T2

def radix_sort(T):
    n = len(T)
    max_len = len(T[0])
    for i in range(max_len-1,-1,-1):
        T = counting_sort_radix(T,i)
    return T


# radix_sort rekurencja

def radix(tab,ind):
    if ind == -1:
        return 0
    
    it = ind
    k = 26
    output = [[] for _ in range(k)]

    for i in tab:
        if len(i) <= it:
            output[0] = [i] + output[0]
        output[ord(i[it])-97].append(i)
    
    sum = []
    for i in output:
        sum += i
    return radix(sum,ind-1)