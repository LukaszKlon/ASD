#quick_sort wykład

# def partition(T,l,r):
#     pivot = T[r]
#     i = l-1
#     for j in range(l,r):
#         if T[j] <= pivot:
#             i += 1
#             T[i],T[j] = T[j],T[i]
#     T[i+1],T[r] = T[r],T[i+1]
#     return i + 1
# def quick_sort(T,l,r):
#     if l < r:
#         q = partition(T,l,r)
#         quick_sort(T,l,q-1)
#         quick_sort(T,q+1,r)


#Quicksort O(log n) pamięci

def partition(T,l,r):
    pivot = T[r]
    i = l-1
    for j in range(l,r):
        if T[j] <= pivot:
            i += 1
            T[i],T[j] = T[j],T[i]
    T[i+1],T[r] = T[r],T[i+1]
    return i + 1
def quick_sort(T,l,r):
    while l < r:
        q = partition(T,l,r)
        if r - q > q - l:
            quick_sort(T,l,q-1)
            l = q + 1
        else:
            quick_sort(T,q+1,r)
            r = q - 1