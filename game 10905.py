#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

Nums = []
flag = True
usados = set()

def game(n,sol):
    global flag
    if n == len(Nums):
        print(sol)
        flag = False
    elif flag:
        i = 0
        while i < (len(Nums)) and flag:
            sol2 = "".join([sol, Nums[i]])
            if not i in usados and sol2 >= "".join([Nums[i] , sol]):
                usados.add(i)
                game(n + 1, sol2)
                usados.remove(i)
            sol2 = sol
            i += 1

def main():
    global Nums,flag
    N = int(stdin.readline())
    while(N != 0):
        flag = True
        Nums = stdin.readline().split()
        Nums.sort(reverse=True)
        game(0, "")
        N = int(stdin.readline())

main()