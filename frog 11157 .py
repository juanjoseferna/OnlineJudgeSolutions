#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

T, N, D = 0,0,0
piedras = []

def frog():
    ans = 0
    n = 0
    SkipS = True
    posiFred = 0
    #IDA
    while(n != N + 1 and posiFred < D):
        if n < N and posiFred < D:
            if piedras[n][0] == 'B':
                if int(piedras[n][2:]) - posiFred > ans:
                    ans = int(piedras[n][2:]) - posiFred
                posiFred = int(piedras[n][2:])
                n += 1
                SkipS = True
            else:
                if SkipS:
                    SkipS = False
                    n += 1
                else:
                    if int(piedras[n][2:]) - posiFred > ans:
                        ans = int(piedras[n][2:]) - posiFred
                    posiFred = int(piedras[n][2:])
                    piedras[n] = 'USADA'
                    n += 1
                    SkipS = True
        elif n == N and posiFred < D:
            if D - posiFred > ans:
                ans = D - posiFred
            posiFred = D
            n += 1
        else:
            n += 1
    #REGRESO
    n = N - 1
    while(n != -1 and posiFred != 0):
        if n > -1 and posiFred > 0:
            if piedras[n][0] == 'B':
                if posiFred - int(piedras[n][2:]) > ans:
                    ans = posiFred - int(piedras[n][2:])
                posiFred = int(piedras[n][2:])
                n -= 1
                SkipS = True
            else:
                if piedras[n] != 'USADA':
                    if posiFred - int(piedras[n][2:]) > ans:
                        ans = posiFred - int(piedras[n][2:])
                    posiFred = int(piedras[n][2:])
                    n -= 1
                    SkipS = True
                else:
                    n -= 1
        elif n == -1 and posiFred > 0:
            if posiFred > ans:
                ans = posiFred
            n -= 1
        else:
            n -= 1
    return ans

def main():
    global T,N,D,piedras
    T = int(stdin.readline())
    for caso in range(1,T + 1):
        piedras = []
        N, D = map(int,stdin.readline().split())
        piedras = stdin.readline().split()
        ans = frog()
        print(f"Case {caso}:",ans)

main()