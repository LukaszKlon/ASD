#sortowanie proste pomocniczo
def insertion_sort(T):
    i = 1
    n = len(T)
    while i < n:
        j = i
        while j > 0 and T[j-1] > T[j]:
            T[j],T[j-1] = T[j-1],T[j]
            j -= 1
        i +=1

#bucket_sort
from math import floor
def bucket_sort(T):
    n = len(T)
    buckets = [[] for _ in range(n)]
    maxi = max(T)+1
    for i in range(n):
        buckets[floor(n*T[i]/maxi)].append(T[i])
    index = 0   
    for i in buckets:
        if len(i) > 1:
            insertion_sort(i)
        for j in i:
            T[index] = j
            index += 1
    return T