import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()


def DFS(graph, v):
    stack = [v]
    visited = [v]

    while stack:
        top = stack.pop()
        if top not in visited:
            visited.append(top)
            stack.extend(graph[top])

    return visited


def BFS(graph, v):
    q = deque([v])
    visited = [False] * (N + 1)

    while q:
        first = q.popleft()
        if first not in visited:
            visited.append(first)
            q.extend(graph[first])

    return visited


for item in DFS(V):
    print(item, end=" ")

print()
for item in BFS(V):
    print(item, end=" ")
