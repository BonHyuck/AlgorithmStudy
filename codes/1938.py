"""
5
B0011
B0000
B0000
11000
EEE00

9
"""


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

visited = [[[0 for _ in range(2)] for _ in range(N)] for _ in range(N)]
logs = [[log]]
visited[log[0]][log[1]][log[2]] = 1
result = 0

while logs:
    queue = []
    possibles = logs.pop()
    found = False
    for row, col, pos in possibles:
        if (row, col, pos) == arrive:
            found = True
            break
        # U
        new_r = row - 1
        new_c = col
        if 0 <= new_r < N and 0 <= new_c < N and visited[new_r][new_c][pos] == 0:
            if pos == 1:
                if 0 <= new_r - 1 < N and box[new_r - 1][new_c] != "1":
                    queue.append((new_r, new_c, pos))
                    visited[new_r][new_c][pos] = 1
            elif pos == 0:
                if 0 <= new_c - 1 < N and 0 <= new_c + 1 < N:
                    if box[new_r][new_c] != "1" and box[new_r][new_c - 1] != "1" and box[new_r][new_c + 1] != "1":
                        queue.append((new_r, new_c, pos))
                        visited[new_r][new_c][pos] = 1
        # D
        new_r = row + 1
        new_c = col
        if 0 <= new_r < N and 0 <= new_c < N and visited[new_r][new_c][pos] == 0:
            if pos == 1:
                if 0 <= new_r + 1 < N and box[new_r + 1][new_c] != "1":
                    queue.append((new_r, new_c, pos))
                    visited[new_r][new_c][pos] = 1
            elif pos == 0:
                if 0 <= new_c - 1 < N and 0 <= new_c + 1 < N:
                    if box[new_r][new_c] != "1" and box[new_r][new_c - 1] != "1" and box[new_r][new_c + 1] != "1":
                        queue.append((new_r, new_c, pos))
                        visited[new_r][new_c][pos] = 1
        # L
        new_r = row
        new_c = col - 1
        if 0 <= new_r < N and 0 <= new_c < N and visited[new_r][new_c][pos] == 0:
            if pos == 0:
                if 0 <= new_c - 1 < N and box[new_r][new_c - 1] != "1":
                    queue.append((new_r, new_c, pos))
                    visited[new_r][new_c][pos] = 1
            elif pos == 1:
                if 0 <= new_r - 1 < N and 0 <= new_r + 1 < N:
                    if box[new_r][new_c] != "1" and box[new_r - 1][new_c] != "1" and box[new_r + 1][new_c] != "1":
                        queue.append((new_r, new_c, pos))
                        visited[new_r][new_c][pos] = 1
        # R
        new_r = row
        new_c = col + 1
        if 0 <= new_r < N and 0 <= new_c < N and visited[new_r][new_c][pos] == 0:
            if pos == 0:
                if 0 <= new_c + 1 < N and box[new_r][new_c + 1] != "1":
                    queue.append((new_r, new_c, pos))
                    visited[new_r][new_c][pos] = 1
            elif pos == 1:
                if 0 <= new_r - 1 < N and 0 <= new_r + 1 < N:
                    if box[new_r][new_c] != "1" and box[new_r - 1][new_c] != "1" and box[new_r + 1][new_c] != "1":
                        queue.append((new_r, new_c, pos))
                        visited[new_r][new_c][pos] = 1
        # T
        new_r = row
        new_c = col
        if 0 <= new_r < N and 0 <= new_c < N:
            if pos == 1 and visited[new_r][new_c][0] == 0:
                if 1 <= new_c < N - 1 and 1 <= new_r < N - 1:
                    if box[new_r][new_c - 1] != "1" and box[new_r][new_c + 1] != "1":
                        if box[new_r - 1][new_c - 1] != "1" and box[new_r - 1][new_c + 1] != "1":
                            if box[new_r + 1][new_c - 1] != "1" and box[new_r + 1][new_c + 1] != "1":
                                queue.append((new_r, new_c, 0))
                                visited[new_r][new_c][0] = 1
            elif pos == 0 and visited[new_r][new_c][1] == 0:
                if 1 <= new_r < N - 1 and 1 <= new_c < N - 1:
                    if box[new_r - 1][new_c] != "1" and box[new_r + 1][new_c] != "1":
                        if box[new_r - 1][new_c - 1] != "1" and box[new_r + 1][new_c - 1] != "1":
                            if box[new_r - 1][new_c + 1] != "1" and box[new_r + 1][new_c + 1] != "1":
                                queue.append((new_r, new_c, 1))
                                visited[new_r][new_c][1] = 1
    if found:
        break
    if len(queue) > 0:
        logs.append(queue)
        result += 1
    else:
        result = 0
        break

print(result)




