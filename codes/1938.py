dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
box = [list(input()) for _ in range(N)]
log = (0, 0, 0)
arrive = (0, 0, 0)
for r in range(N):
    for c in range(N):
        if box[r][c] == "B":
            for k in range(4):
                new_r = r + dr[k]
                new_c = c + dc[k]
                if 0 <= new_r < N and 0 <= new_c < N:
                    if box[new_r][new_c] == "B":
                        if k < 2:
                            log = (new_r, new_c, 1)
                        else:
                            log = (new_r, new_c, 0)
                        break
            break

for r in range(N):
    for c in range(N):
        if box[r][c] == "E":
            for k in range(4):
                new_r = r + dr[k]
                new_c = c + dc[k]
                if 0 <= new_r < N and 0 <= new_c < N:
                    if box[new_r][new_c] == "E":
                        if k < 2:
                            arrive = (new_r, new_c, 1)
                        else:
                            arrive = (new_r, new_c, 0)
                        break
            break

print(log)
print(arrive)

visited = [[[0 for _ in range(2)] for _ in range(N)] for _ in range(N)]
logs = [[log]]
visited[log[0]][log[1]][log[2]] = 1
result = 0

while logs:
    queue = []
    possibles = logs.pop()
    for row, col, pos in possibles:
        # U
        




