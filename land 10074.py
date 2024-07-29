#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

N = 0
M = 0
matriz = []

def convMat():
    for i in range(N):
        for j in range(M):
            if matriz[i][j] == 1:
                matriz[i][j] = -float('inf')
            #elif j > 0:
            #    matriz[i][j] = max(matriz[i][j - 1] + matriz[i][j] + 1, matriz[i][j] + 1 )
            else:
                matriz[i][j] = 1

def phinchi(A):
    maximo = A[0]
    phi = A[0]
    for i in range(1,len(A)):
        phi = max(phi + A[i],A[i])
        maximo = max(maximo,phi)
    return maximo

def land():
    low, hi= 0,0
    sumaActual, sumaMaxima = 0,0
    temp = [0 for _ in range(N)]
    memo = {}
    while low != M:
        for i in range(N):
            if low == hi:
                temp[i] = matriz[i][hi]
            else:
                temp[i] = matriz[i][hi] + temp[i]
        if tuple(temp) in memo :
            sumaActual= memo[tuple(temp)]
        else:
            sumaActual = phinchi(temp)
            memo[tuple(temp)] = sumaActual
        if sumaActual > sumaMaxima:
            sumaMaxima = sumaActual
        if hi == M - 1:
            low,hi = low + 1, low + 1
        else:
            hi += 1
    return sumaMaxima

    
def main():
    global N,M,matriz
    N,M = map(int,stdin.readline().split())
    while(N != 0):
        matriz = []
        for i in range(N):
            matriz.append(list(map(int,stdin.readline().split())))
        convMat()
        print(land())
        N,M = map(int,stdin.readline().split())

main()
