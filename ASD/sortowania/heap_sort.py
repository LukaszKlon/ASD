#heap_sort

def heapify(T,i,j):
    maks = i
    # l = left(i)
    # r = right(i)
    l = 2*i+1
    r = 2*i+2
    if l < j and T[l] > T[maks]: maks = l
    if r < j and T[r] > T[maks]: maks = r
    if maks != i:
        T[i],T[maks] = T[maks],T[i]
        heapify(T,maks,j)

def buildheap(T):
    n = len(T)
    x = (n-2)//2
    for i in range(x,-1,-1):
        heapify(T,i,n)
T = [45,2,77,8,23,1,77,5648,1234,3,22]

def heap_sort(T):
    n = len(T)
    buildheap(T)
    for i in range(1,n):
        T[n-i],T[0] = T[0],T[n-i]
        heapify(T,0,n-i)
    return T
T = heap_sort(T)
print(T)