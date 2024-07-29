#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin
from heapq import heappush,heappop


def agregarVenta(buy,sell,history): #Venta, Compra Historial
    if(len(buy) != 0 and len(sell) != 0):
        if(abs(buy[0][0]) >= sell[0][0]):
            if(buy[0][1] < sell[0][1]):
                tmp = heappop(buy)
                sell[0][1] -= tmp[1]
                history.append(sell[0])
                return agregarVenta(buy,sell,history)
            elif(buy[0][1] == sell[0][1]):
                tmp = heappop(sell)
                heappop(buy)
                history.append(tmp)
                return buy,sell,history
            elif(buy[0][1] > sell[0][1]):
                tmp = heappop(sell)
                buy[0][1] = buy[0][1] - tmp[1]
                history.append(tmp)
                return agregarVenta(buy,sell,history)
    return buy,sell,history

def main():
    n = int(stdin.readline())
    for _ in range(n):
        n2 = int(stdin.readline())
        buy = []
        sell = []
        history = []
        for _ in range (n2):
            n3 = stdin.readline().split()
            if (n3[0] == "sell"):
                heappush(sell,[int(n3[-1]),int(n3[1])])
                buy,sell,history = agregarVenta(buy,sell,history)
            elif(n3[0] == "buy"):
                heappush(buy,[-int(n3[-1]),int(n3[1])])
                buy,sell,history = agregarVenta(buy,sell,history)
            if(len(sell) > 0):
                output = [str(sell[0][0])]
            else:
                output = ["-"]
            if(len(buy) > 0):
                output.append(str(abs(buy[0][0])))
            else:
                output.append("-")
            if(len(history) > 0):
                output.append(str(history[-1][0]))
            else:
                output.append("-")
            
            print(output[0],output[1],output[2])

main()