#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin
from heapq import heappush,heappop

pedidos = []
N = 0

def customer ():
    ans = 0
    time = 0
    aceptados = []
    for i in range(N):
        if time + pedidos[i][0] <= pedidos[i][1]:
            heappush(aceptados,-pedidos[i][0])
            time += pedidos[i][0]
        else:
            heappush(aceptados,-pedidos[i][0])
            time += pedidos[i][0]
            time += heappop(aceptados)
    ans = len(aceptados)
    aceptados = []
    return ans

def main():
    global pedidos, N
    casos = int(stdin.readline())
    for _ in range (casos):
        stdin.readline()
        N = int(stdin.readline())
        pedidos = []
        for _ in range(N):
            pedidos.append(list(map(int,stdin.readline().split())))
        pedidos.sort(key= lambda x: x[1])
        print(customer())
        print()
        

main()