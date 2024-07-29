#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin
from time import sleep

S = 0
N = 0
data = {}
usados = {}
lista2 = []
memo = {}
maximos = []

def busquedaBin(lista, x):
    low = 0
    hi = len(lista) - 1
    ind = -1

    while low <= hi:
        mid = (low + hi) // 2 

        if lista[mid] <= x:
            ind = mid 
            low = mid + 1  
        else:
            hi = mid - 1 
    return ind

def stampsAux(n,nums,j):
    if n in memo[j]:
        ans = memo[j][n]
    else:
        i = busquedaBin(nums,n) 
        if n < nums[0]:
            ans = 0
        elif i + 1 <= 1:
            ans = n
        else:
            lista = []
            for x in range(i,-1,-1):
                lista.append(stampsAux(n - nums[x],nums,j) + 1)
            ans = min(lista)
            memo[j][n] = ans
    return ans

def stamps(n,j,r):
    ans = stampsAux(n,data[j],j)
    if ans <= S and ans != 0:
        stamps(n + 1,j,r)
    else:
        maximos.append(n - 1 - (r/100))

def cualImprimirAux(maxI):
    res = maxI.pop()
    ultimo = data[res]
    for i in maxI:
        j = -1
        ans = None
        while abs(j) <= len(ultimo) and ans == None:
            if ultimo[j] > data[i][j]:
                ans = i
                res = ans
                ultimo = data[i]
            elif ultimo[j] < data[i][j]:
                ans = res
            else:
                j -= 1
    return ans

def cualImprimir():
    max_valor = maximos[0]
    max_indices = [0]    
    for i in range(1, len(maximos)):
        if maximos[i] > max_valor:
            max_valor = maximos[i] 
            max_indices = [i]
        elif maximos[i] == max_valor:
            max_indices.append(i)
    if len(max_indices) == 1:
        ans = max_indices[0]
    else:
        ans = cualImprimirAux(max_indices)
    return ans

def imprimir():
    ans = cualImprimir()
    ArForm = [f"{e:3d}" for e in data[ans]]
    maximos[ans] = round(maximos[ans])
    tmp = f"".join(map(str, ArForm))
    print(f"max coverage = {maximos[ans]:3d} :{tmp}")

def main():
    global S,N,data,memo,maximos,usados
    S = int(stdin.readline())
    while (S != 0):
        data = {}
        usados = {}
        maximos = []
        N = int(stdin.readline())
        for i in range(N):
            memo[i] = {}
            data[i] = list(map(int,stdin.readline().split()))
            r = data[i].pop(0)
            stamps(1,i,r)
        imprimir()
        S = int(stdin.readline())

main()