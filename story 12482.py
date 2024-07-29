#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

texto = []

def story(N,L,C):
    n = 0
    pag = 1
    l = 1
    c = 0
    while(n != N):
        if c + texto[n] + 1 <= C:
            c += texto[n] + 1
            n += 1
        elif c + texto[n] == C:
            c = 0
            n += 1
            if l == L and n != N:
                l = 1
                pag += 1
            else:
                l += 1
        else:
            c = 0
            if l == L:
                l = 1
                pag += 1
            else:
                l += 1
    return pag

def main():
    global texto
    entrada = stdin.readline()
    while entrada != '' and entrada != '\n':
        N,L,C = map(int,entrada.split())
        texto = list(map(len,stdin.readline().split()))
        print(story(N,L,C))
        entrada = stdin.readline()

main()
