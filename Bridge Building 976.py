#
#   Por: Juan José Fernández Aristizábal 🐨 - Cód: 8953371
#   Proyecto ADA 2023-2
#   Octubre - Noviembre 2023
#   Pontificia Universidad Javeriana Cali
#   Ingeniería de Sistemas y Computación
#   UVa 976 - Bridge Building
#   Versión final
#
from sys import stdin, setrecursionlimit
# Se decidio aumentar el limite de recursión para que se pueda ejecutar el programa sin problemas con entradas 1000x1000.
setrecursionlimit(1000000)

R,C,B,S,memo,distancias = 0,0,0,0,{},[]

'''
La función floodFill es una función recursiva que recorre la matriz, y cada vez que encuentra un #, lo cambia por un A, y hace una llamada 
recursiva a la función en las cuatro direcciones posibles, arriba, abajo, izquierda y derecha, si la posición a la que se quiere mover no es un #,
la función no hace nada.

Su complejidad es O(R * C) ya que en el peor de los casos se recorre casi toda la matriz y su complejidad espacial es O(1) ya que no se usa 
memoria adicional.

Entrada: Una matriz de caracteres, una fila y una columna.

Salida: Ninguna.
'''

def floodFill(matriz, fila, columna):
        matriz[fila][columna] = 'A'
        if fila - 1 > 0 and matriz[fila - 1][columna] == '#':
            floodFill(matriz, fila - 1, columna)
        if columna - 1 > 0 and matriz[fila][columna - 1] == '#':
            floodFill(matriz, fila, columna - 1)
        if fila + 1 < R and matriz[fila + 1][columna] == '#':
            floodFill(matriz, fila + 1, columna)
        if columna + 1 < C and matriz[fila][columna + 1] == '#':
            floodFill(matriz, fila, columna + 1)

'''
La función medirPuente es una función que recorre la matriz por filas, en cada fila, la función recorre la columna de arriba hacia abajo,
si encuentra un A, la distancia se reinicia a 0, ya que se esta midiendo la distancia entre 'A' y '#', si encuentra un #, la función retorna la 
distancia que va aumentando en cada iteración, si no encuentra ni A ni #, la distancia aumenta en 1.

Su complejidad es O(R * C) ya que se hace se llama a la función tantas veces como columnas tiene la matriz y su complejidad espacial es O(C) ya 
que se usa un lista para guardar las distancias de cada columna (esto se hace en el main).

Entrada: Una matriz de caracteres y una columna.

Salida: Una lista de enteros, donde cada posición representa la distancia entre un 'A' y un '#' de cada columna.
'''

def medirPuente(matriz, columna):
    ans = 0
    fila = 0
    salida = False
    while fila < R and not salida:
        if matriz[fila][columna] == 'A':
            ans = 0
        elif matriz[fila][columna] == '#':
            salida = True
        else:
            ans += 1
        fila += 1
    return ans

'''
La función bridgeBuilding es la función objetivo que usa programación dinámica, tiene dos casos base, el primero es cuando B es igual a 0, es decir,
cuando ya se pusieron todos los puentes, y el otro caso base es cuando columna es mayor o igual a C, es decir, cuando se salió de la matriz sin
poner todos los puentes, en este caso se retorna infinito, ya que no se puede poner un puente en una columna que no existe. Si no se cumple ninguno de
los casos base, se hace una llamada recursiva a la función, en la primera llamada se pone un puente en la columna, y se vuelve a llamar a la función
avanzando S + 1 columnas, y se le resta 1 a B, y se le suma la distancia (que se calculo en la función medirPuente) lo que significa que se puso 
un puente, y en la segunda llamada se avanza a la siguiente columna sin poner un puente, y se le deja el mismo valor a B, y se retorna el mínimo 
entre las dos llamadas recursivas.

Entrada: Distancia[0..C), dos enteros B y S, donde B es el numero de puentes que se deben poner y S es la distancia mínima entre dos puentes.

Salida: Un entero que representa la mínima longitud total de los puentes que se pueden construir.

Φ(fila, B, S) = "La mínima longitud total de los puentes que se pueden construir".

                0, si B = 0
Φ(fila, B, S) = ∞, si fila ≥ C
                min(Φ(fila + S + 1, B - 1, S) + distancias[fila], Φ(fila + 1, B, S))
            
Entrada: Distancia[0..n), dos enteros B y S, donde B es el numero de puentes que se deben poner y S es la distancia mínima entre dos puentes.

Salida: Φ(0, B, S)

Es facíl ver que es muy parecido al problema de la mochila, ya que se tiene un numero de objetos (columnas) y se quiere maximizar el valor (minimizar la longitud total de los puentes)
de los objetos que se pueden poner en la mochila (se pueden poner puentes en las columnas), entonces su complejidad es similar a la del problema de la mochila, es decir,
O(C * B) y su complejidad espacial es O(C * B) ya que se usa un diccionario para guardar los valores que ya se calcularon y no volver a calcularlos.
'''

def bridgeBuilding(columna, B, S):
    global memo
    if (columna,B) in memo:
        ans = memo[(columna,B)]
    else:
        ans = 0
        if B == 0:
            ans = 0
        elif columna >= C:
            ans = float('inf')
        else:
            ans = min(bridgeBuilding(columna + S + 1, B - 1, S) + distancias[columna], bridgeBuilding(columna + 1, B, S))
            memo[(columna,B)] = ans
    return ans

'''
La función principal main, lee la entrada, crea la matriz, llama a la función floodFill, y luego a la función bridgeBuilding, e imprime la respuesta.
'''

def main():
    global R, C, B, S, memo, distancias
    entrada = stdin.readline()
    while entrada != "" and entrada != "\n":
        R, C = map(int, entrada.split())
        matriz = []
        memo = {}
        distancias = []
        B, S = map(int, stdin.readline().split())
        for i in range(R):
            matriz.append(list(stdin.readline()))
        floodFill(matriz, 0, 0)
        for i in range(C):
            distancias.append(medirPuente(matriz, i))
        print(bridgeBuilding(0, B, S))
        entrada = stdin.readline()

main()

'''
Código de honor:
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
'''

'''
La complejidad del algoritmo flood fill es O(R * C) ya que se recorre toda la matriz y se llama a la función bridgeBuilding que tiene complejidad 
O(C * B) y su complejidad espacial es O(C * B) ya que se usa un diccionario para guardar los valores que ya se calcularon y no volver a calcularlos
y una lista para guardar las distancias de cada columna O(C).

En total el algoritmo tiene complejidad O(R * C + C * B), es decir, O(R * C) ya que C es mayor que B y su complejidad espacial es O(C * B + C), es
decir, O(C * B) ya que C es menor que C * B.
'''