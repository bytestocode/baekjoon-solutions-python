import sys
input = sys.stdin.readline

N = int(input())
input_list = [0] * 10001

for _ in range(N):
    input_list[int(input())] += 1

for i in range(10001):
    while input_list[i] > 0:
        print(i)
        input_list[i] -= 1
