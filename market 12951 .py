#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin,setrecursionlimit

setrecursionlimit(200000)

N = 0
C = 0
p = []
memo = {}

def market(n, comprando = 0):
    ans = None
    if (n,comprando) in memo: ans = memo[(n,comprando)]
    else:
        if n == N: ans = 0
        else:
            if comprando == 0: ans = max(market(n + 1), market(n + 1,1) - p[n] - C)
            else:
                ans = max(market(n + 1) + p[n], market(n + 1,comprando))
        memo[(n,comprando)] = ans
    return ans


def main():
    global N,C,p,memo
    N, C = 0,0
    entrada = stdin.readline()
    while(entrada != "" and entrada != "\n"):
        memo = {}
        N,C = map(int,entrada.split())
        p = list(map(int,stdin.readline().split()))
        print(market(0))
        entrada = stdin.readline()

main()