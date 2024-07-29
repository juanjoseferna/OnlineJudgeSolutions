#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

def binarySearchIter(A, v,low,hi, ans):
    res = [A[low],v]
    contador = 0
    while hi - low > 1:
        mid = (hi + low) // 2
        if A[mid] <= v:
            contador += mid - low
            low = mid
            res[1] = A[mid]
        else:
            hi = mid
    if A[low] <= v:
        contador += 1
        res[1] = A[low]
    res.append(contador)
    if(res[2] > ans[2]):
        return res
    return ans

def solve(popes,N,Y):
    ans = [0,0,0]
    for i in range(N):
        v = Y + popes[i] - 1
        ans = binarySearchIter(popes,v,i,N,ans)
    print(ans[2],ans[0],ans[1])

def main():
    Y = stdin.readline()
    while(Y != ""):
        Y = int(Y)
        N = int(stdin.readline())
        popes = []
        for _ in range(N):
            popes.append(int(stdin.readline()))
        solve(popes,N,Y)
        stdin.readline()
        Y = stdin.readline()

main()