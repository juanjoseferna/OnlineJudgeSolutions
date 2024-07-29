#
#   Por: Juan José Fernández Aristizábal 🐨
#
from math import ceil
from sys import stdin

def LAP():
    n = stdin.readline()
    while(n != "" and n != "\n"):
        X,Y = map(int,n.split())
        velX = 1/X
        velY = 1/Y
        salida = True
        segundos = 0
        while (salida):
            segundos += 1
            if(velX * segundos >= (velY*segundos) + 1):
                salida = False
        print(ceil(velX * segundos))
        n = stdin.readline()


LAP()