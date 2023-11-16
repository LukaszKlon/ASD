def partition(T,l,r):
    pivot = T[r]
    j = l-1
    for i in range(l,r):
        if T[i] <= pivot:
            j += 1
            T[j],T[i] = T[i],T[j]
    T[r],T[j+1] = T[j+1],T[r]
    return j + 1
def quick_select(T,l,r,k):
    if l < r:
        pivot = partition(T,l,r)
        if k < pivot:
            quick_select(T,l,pivot-1,k)
        elif k > pivot:
            quick_select(T,pivot+1,r,k)