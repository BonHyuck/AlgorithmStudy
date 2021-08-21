import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
plants = list(map(int, input().split()))
connection = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for k in range(M):
    u, v, w = map(int, input().split())
    connection[u][v] = w
    connection[v][u] = w

cable = [10001 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
for k in plants:
    cable[k] = 0
while plants:
    plant = plants.pop(0)
    visited[plant] = 1
    for next_plant in range(1, N + 1):
        if connection[plant][next_plant] > 0 and visited[next_plant] == 0:
            cable[next_plant] = min(connection[plant][next_plant], cable[next_plant])
            plants.append(next_plant)
print(cable)
