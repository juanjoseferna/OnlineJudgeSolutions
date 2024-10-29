#
#   Por: Juan José Fernández Aristizábal 🐨
#
from sys import stdin

def binary_search(lista, target):
    ans = -1
    left = 0
    right = len(lista) - 1
    while left <= right and ans == -1:
        mid = (left + right) // 2
        if lista[mid] == target:
            ans = mid
        elif lista[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans

def exact_sum(n, books, m):
    books.sort()
    i = 0
    ans = []
    while i < n:
        if binary_search(books, m - books[i]) not in [-1, i]:
            ans.append((books[i], m - books[i]))
        i += 1
    i,j = ans[0]
    for a in range(len(ans)):
        if abs(ans[a][1] - ans[a][0]) < abs(j - i):
            i,j = ans[a]
    if i > j:
        i,j = j,i
    return i,j

def main():
    n = stdin.readline()
    while n != '' and n != '\n':
        n = int(n)
        books = list(map(int, stdin.readline().split()))
        m = int(stdin.readline())
        i,j = exact_sum(n, books, m)
        print('Peter should buy books whose prices are {} and {}.'.format(i, j))
        print()
        stdin.readline()
        n = stdin.readline()
main()