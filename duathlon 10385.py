#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

runners = 0
tramposo = 0
total = 0

def solve(func, min, max):
    eps=10**-6
    mid1 = min + (max - min)/3
    mid2 = max - (max - min)/3
    if max-min < eps:
        return [round(func((min +max)/2)),(min+max)/2]
    if func(mid1) < func(mid2):
        return solve(func,mid1,max)
    else:
        return solve(func,min,mid2)

def funcion(d):
  tRunners = []
  tTramposo = d/tramposo[0] +  (total - (d))/tramposo[1]
  for i in runners:
     tRunners.append(d/i[0] + (total - d)/i[1])
  rapido = min(tRunners)
  return (rapido - tTramposo) * 3600

def main():
    global runners, tramposo, total
    total= stdin.readline()
    tmp = "\n"
    while(tmp == "\n" and total != ""):
        total= int(total)
        totalCorredores = int(stdin.readline())
        runners = []
        for _ in range (totalCorredores - 1):
            vr,vk = map(eval,stdin.readline().split())
            runners += [[vr,vk]]
            #Distancia corriendo + Distancia restante
        vr,vk = map(eval,stdin.readline().split())
        tramposo = [vr,vk]
        ans = solve(funcion,0,total)
        ans.append(total - ans[-1])
        if ans[0] < 0.0: print('The cheater cannot win.')
        else: print('The cheater can win by {0} seconds with r = {1:.2f}km and k = {2:.2f}km.'.format(ans[0], ans[1], ans[2]))
        tmp = stdin.readline()
        total= stdin.readline()

main()