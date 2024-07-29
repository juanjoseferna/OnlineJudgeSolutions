#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin
from math import factorial

sols = []
factCad = 0

def permuted(n,cad,i,sol):
    global count,sols
    if n == len(cad):
        sols.append(list(sol))
    elif len(sols) < 1:
        for j in range(len(sol) + 1):
            sol.insert(j,cad[n])
            factSol = factorial(len(sol))
            divFacts = factCad//factSol
            if count < i  and i <= count + divFacts:
                permuted(n + 1,cad,i,sol)
            else:
                count += divFacts
            sol.pop(j)

def main():     
    global sols, count, factCad, count
    casos = int(stdin.readline())
    for _ in range(casos):
        count = 0
        sols = []
        cad = stdin.readline().strip()
        factCad = factorial(len(cad))
        i = int(stdin.readline())
        sol = []
        permuted(0,cad,i,sol)
        #print(sols)
        print(''.join(sols[0]))

main()