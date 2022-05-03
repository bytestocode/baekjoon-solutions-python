import sys
input = sys.stdin.readline
import math

result = []


def c(min, max):
    cnt = 0
    check = [True] * (max + 1)

    for i in range(2, int(math.sqrt(max) + 1)):
        if check[i] == True:
            for j in range(i * 2, max + 1, i):
                check[j] = False

    for i in range(min + 1, max + 1):
        if check[i] == True:
            cnt += 1
    return cnt


while True:
    n = int(input())
    if n == 0:
        break
    result.append(c(n, 2 * n))

for num in result:
    print(num)
