# mergesort

# def merge_sort(T):
#     print(T)
#     n = len(T)
#     if n == 1:
#         return T
#     # scal
#     Left = merge_sort(T[:n//2])
#     Right = merge_sort(T[n//2:])
#     # print(Left)
#     dl = len(Left)
#     dp = len(Right)
#     l = 0
#     p = 0
#     i = 0
#     while l < dl and p < dp:
#         if Left[l] < Right[p]:
#             T[i] = Left[l]
#             l += 1
#         else:
#             T[i] = Right[p]
#             p += 1
#         i += 1
#     if l == n//2:
#         while i < n:
#             T[i] = Right[p]
#             i += 1
#             p += 1
#     else:
#         while i < n:
#             T[i] = Left[l]
#             i += 1
#             l += 1
#     print(T)
#     return T

# sortowanie w miejscu

def obrot(T,l,r):
    for i in range(r,l,-1):
        T[i],T[i-1] = T[i-1],T[i]
        
def merge(T,l,r,s):
    n = len(T)
    while l < s+1 and s+1 <= r:
        if T[l] > T[s+1]:
            obrot(T,l,s+1)
            l += 1
            s += 1
        else:
            l += 1
def merge_sort(T,l,r):
    if l < r:
        s = (l+r)//2
        merge_sort(T,l,s)
        merge_sort(T,s+1,r)
        merge(T,l,r,s)