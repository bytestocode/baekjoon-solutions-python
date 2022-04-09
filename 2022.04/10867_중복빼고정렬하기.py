import sys
input = sys.stdin.readline

N = int(input())
input_list = list(set(map(int, input().split())))

input_list.sort()

for el in input_list:
    print(el, end=' ')
