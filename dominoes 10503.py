#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

M = 0
N = 0
ans = False
usadas = set()

def check(ficha,sol,n):
    ans = 0
    if ficha[0] == sol[n - 1][1]:
        if n == N:
            if ficha[1] == sol[n + 1][0] : # or ficha[1] == sol[n + 1][1]
                ans = 1
        else:
            ans = 1
    elif ficha[1] == sol[n - 1][1]:
        if n == N:
            if ficha[0] == sol[n + 1][0] : # or ficha[0] == sol[n + 1][1]
                ans = 2
        else:
            ans = 2
            
    return ans

def dominoes(n,fichas,sol):
    global ans
    if n == N + 1:
        ans = True
        # print(sol)
        # print(True)
    elif not ans:
        for ficha in fichas:
            tmp = check(ficha,sol,n)
            if not ficha in usadas and tmp > 0:
                usadas.add(ficha)
                if tmp == 1:
                    sol[n] = ficha
                else:
                    sol[n] = ficha[::-1]
                # print(sol)
                dominoes(n + 1, fichas, sol)
                usadas.remove(ficha)

def main():
    global M, N, ans, usadas
    N = int(stdin.readline())
    while N != 0:
        usadas = set()
        ans = False
        M = int(stdin.readline())
        ini = tuple(map(int,stdin.readline().split()))
        fin = tuple(map(int,stdin.readline().split()))
        fichas = []
        for i in range(M):
            fichas.append(tuple(map(int,stdin.readline().split())))
        sol = [None for _ in range(N + 2)]
        sol[0] = ini
        sol[-1] = fin
        dominoes(1,fichas,sol)
        if ans:
            print("YES")
        else:
            print("NO")
        N = int(stdin.readline())

main()