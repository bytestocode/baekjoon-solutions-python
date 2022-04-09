import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(graph, a, b):
    q = deque()
    q.append([a, b])

    while q:
        [x, y] = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx, ny])
    return


for _ in range(T):
    M, N, K = map(int, input().split())
    count = 0

    graph = [[0] * N for _ in range(M)]

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                count += 1

    print(count)
