#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

dishes = {}
memo = {}
N = 0
x = 0
T = 0
K = 0
cuenta = 0
memo = {}

def yumcha(k,totalDishes,Pres):
    ans = None
    if (k,totalDishes,Pres) in memo:
        ans = memo[(k,totalDishes,Pres)]
    else:
        if k == K or totalDishes < 0:
            ans = 0
        else:
            if x*(N+1) -(Pres + dishes[k]['Precio']*2)*1.1 >= 0 and totalDishes >= 2:
                ans = max(yumcha(k + 1,totalDishes,Pres),
                    yumcha(k + 1,totalDishes - 1, Pres + dishes[k]['Precio']) + dishes[k]['Valoracion'],
                    yumcha(k + 1,totalDishes - 2, Pres + dishes[k]['Precio']*2) + dishes[k]['Valoracion']*2)
            elif x*(N+1) -(Pres + dishes[k]['Precio'])*1.1 >= 0 and totalDishes >= 1:
                ans = max(yumcha(k + 1,totalDishes,Pres),
                    yumcha(k + 1,totalDishes - 1, Pres + dishes[k]['Precio']) + dishes[k]['Valoracion'])
            else:
                ans = yumcha(k + 1,totalDishes,Pres)
            memo[(k,totalDishes,Pres)] = ans
    #print(k,totalDishes,Pres,ans)
    return ans
        

def main():
    global dishes,N,x,T,K,memo
    N,x,T,K = map(int,stdin.readline().split())
    while (N != 0):
        for i in range(K):
            tmp = list(map(int,stdin.readline().split()))
            dishes[i] = {}
            dishes[i]['Precio']= tmp.pop(0)
            dishes[i]['Valoracion'] = sum(tmp)/(N + 1)
        memo = {}
        print(f'{(yumcha(0,2*(N+1),T*(N+1))):.2f}')
        entrada = stdin.readline()
        N,x,T,K = map(int,entrada.split())
        
main()