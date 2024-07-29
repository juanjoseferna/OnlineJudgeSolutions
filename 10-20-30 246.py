#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin
from collections import deque

WINNERS = [10,20,30]

def jugar(mano,juego,njuegos,i):
    if(len(juego[i]) >= 3):
        if(sum([juego[i][0],juego[i][1],juego[i][-1]]) in WINNERS):
            mano.append(juego[i].pop(0))
            mano.append(juego[i].pop(0))
            mano.append(juego[i].pop())
            if(len(juego[i]) == 0):
                njuegos-= 1
                juego.pop(i)
                i -= 1
            else:
                return jugar(mano,juego,njuegos,i)
                
        elif(sum([juego[i][0],juego[i][-1],juego[i][-2]]) in WINNERS):
            mano.append(juego[i].pop(0))
            tmp = juego[i].pop()
            mano.append(juego[i].pop())
            mano.append(tmp)
            if(len(juego[i]) == 0):
                njuegos-= 1
                juego.pop(i)
                i -= 1
            else:
                return jugar(mano,juego,njuegos,i)
            
        elif(sum([juego[i][-1],juego[i][-2],juego[i][-3]]) in WINNERS):
            tmp1 = juego[i].pop()
            tmp2 = juego[i].pop()
            mano.append(juego[i].pop())
            mano.append(tmp2)
            mano.append(tmp1)
            if(len(juego[i]) == 0):
                njuegos-= 1
                juego.pop(i)
                i -= 1
            else:
                return jugar(mano,juego,njuegos,i)
    return mano,juego,njuegos,i

def main ():
    entrada = stdin.readline()
    while(entrada[0] != "0"):
        mano = deque()
        while(len(mano) < 52):
            entrada = list(map(int,entrada.split()))
            mano.extend(entrada)
            if(len(mano) < 52):
                entrada = stdin.readline()
        juego = []
        njuegos = 7
        score = 7
        for i in range(njuegos):
            juego.append([mano.popleft()])
        salida = False
        estado = str(mano) + str(juego)
        estados = set()
        while(not(salida)): 
            i = 0
            while(i < njuegos and not(salida)):
                estados.add(estado)
                juego[i].append(mano.popleft())
                mano,juego,njuegos,i = jugar(mano,juego,njuegos,i)
                i += 1
                estado = str(mano) + str(juego)
                score = score + 1
                if(len(mano) == 0):
                    salida = True
                    print("Loss:",score)
                elif(len(mano) == 52):
                    salida = True
                    print("Win :",score)
                elif(estado in estados):
                    salida = True
                    print("Draw:",score)
        entrada = stdin.readline()

main()