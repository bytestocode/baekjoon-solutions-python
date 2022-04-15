import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            tri_sum = cards[i] + cards[j] + cards[k]
            if tri_sum <= M:
                result = max(tri_sum, result)

print(result)
