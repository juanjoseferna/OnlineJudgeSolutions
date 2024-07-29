#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

arbol = []

def bst(Fin,H,Ini = 1):
    n = Ini
    ans = True
    while(n <= Fin and ans and H >= 0):
        if Fin - n <= 2**H - 1 and n - Ini <= 2**H - 1:
            arbol.append(n)
            bst(n - 1,H - 1,Ini)
            bst(Fin,H - 1,n + 1)
            ans = False
        else:
            n += 1
    return arbol

def main():
    global arbol
    N,H = map(int,stdin.readline().split())
    caso = 1
    while N != 0:
        arbol = []
        if 2**H - 1 < N:
            print(f"Case {caso}:", "Impossible.")
        else:
            print(f"Case {caso}:", *bst(N,H - 1))
        N,H = map(int,stdin.readline().split())
        caso += 1

main()