import sys
input = sys.stdin.readline
import math

N = int(input())

for _ in range(N):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())

  if (x1 == x2 and y1 == y2):
    if (r1 == r2):
      print(-1)
    else:
      print(0)
  else:
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if (abs(r1 - r2) < distance < r1 + r2):
      print(2)
    elif (abs(r1 - r2) == distance or distance == r1 + r2):
      print(1)
    else:
      print(0) 