def counting_sort(T):
    n = len(T)
    k = max(T) + 1
    TMP = [0 for _ in range(k)]
    T2 = [0 for _ in range(n)]
    for i in T:
        TMP[i] += 1
    for i in range(1,k):
        TMP[i] += TMP[i-1]
    for i in range(n-1,-1,-1):
        T2[TMP[T[i]]-1] = T[i]
        TMP[T[i]] -= 1
    return T2