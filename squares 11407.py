#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

def squares(N,i,memo):
    if N in memo:
        ans = memo[N]
    else:
        ans = None
        if( i <= 1):
            ans = N 
        else:
            ans = min(squares(N - i ** 2, ((N - i ** 2)**(0.5))//1,memo) + 1,squares(N,i - 1,memo) )
            ans = int(ans)
            memo[int(N)] = ans
    return ans

'''
def squaresTab(N):
    tabla = [0 for _ in range(10001)] 
    for i in range (1,10001):
        tabla[i] = min(tabla[i-1] + 1, tabla[int(i**0.5)] + 1)
    return tabla
'''
def main():
    casos = int(stdin.readline())   
    memo = {0:0,1:1}
    for _ in range(casos):
        N = int(stdin.readline())
        print(squares(N,(N**(0.5))//1,memo))

main()