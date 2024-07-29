#
#   Por: Juan José Fernández Aristizábal 🐨
#

def merge(A, low, mid, hi,inversions):
    global tmp
    for i in range(low, hi):
        tmp[i] = A[i]
    l, r = low, mid
    for n in range(low, hi):
        if (l == mid):
            A[n] = tmp[r]
            r += 1
        elif (r == hi):
            A[n] = tmp[l]
            l += 1
        else:
            if (tmp[l] <= tmp[r]):
                A[n] = tmp[l]
                l += 1
            else:
                A[n] = tmp[r]
                inversions += (mid - l)
                # print(inversions,mid,l)
                r += 1
    return inversions

def mergesort(A,low, hi,inversions):
    if (low + 1< hi):
        mid = low +((hi - low) >> 1) 
        inversions += mergesort(A,low,mid,0)
        inversions += mergesort(A,mid,hi,0)
        inversions += merge(A,low,mid,hi,0)
        return inversions
    return 0

def inver ():
    global tmp
    n = int(input())
    while (n != 0):   
        A = []
        tmp = [None for _ in range(n)]
        for i in range(0,n):
            A.append(int(input()))
        inversions =mergesort(A,0,n,0)
        print(inversions)
        n = int(input())

tmp = []
inversions = 0
inver()