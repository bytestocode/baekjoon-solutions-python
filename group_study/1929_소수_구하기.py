import sys
input = sys.stdin.readline
import math

M, N = map(int, input().split())

def prime(num):
  if num == 1:
    return
  elif num == 2:
    print(num)
  else:
    i = 2
    while (True):
      if (i <= int(math.sqrt(num) + 1)):
        if (num % i == 0):
          break
        else:
          i += 1
      else:
        print(num)
        break



for num in range(M, N + 1):
  prime(num)

