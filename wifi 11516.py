#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

def aux(mid,casas,ncasas,routers):
    ans = False
    i, j, rango = 0,0,0
    while(i < routers and j < ncasas):
        rango = mid + casas[j]
        j += 1
        while(j < ncasas and casas[j] <= rango):
            j += 1
        i += 1
    if j == ncasas:
        ans = True
    return ans

def binarySearch(casas,ncasas,routers):
    low = 0
    hi = casas[-1]
    while hi - low > 1:
        mid = low + ((hi - low) >>1)
        if aux(mid,casas,ncasas,routers):
            hi = mid
        else:
            low = mid
    print(f'{hi/2:.1f}')

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        casas = []
        routers, ncasas = map(int,stdin.readline().split())
        for i in range(ncasas):
            casas.append(int(stdin.readline()))
        casas.sort()
        if(routers >= ncasas):
            print("0.0")
        else:
            binarySearch(casas,ncasas,routers)

main()