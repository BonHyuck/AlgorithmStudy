N, M = map(int, input().split())
connections = [[0 for _ in range(N+1)] for _ in range(N+1)]
for k in range(M):
    x, y = map(int, input().split())
    connections[x][y] = 1
    connections[y][x] = 1

for number in range(1, N+1):
    

