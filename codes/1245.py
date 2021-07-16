# 1245. [S1] 농장관리
# https://www.acmicpc.net/problem/1245
import sys

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def find_mountain(row, col):
    global top
    for k in range(8):
        new_r = row + dx[k]
        new_c = col + dy[k]
        if 0 <= new_r < N and 0 <= new_c < M:
            if box[row][col] < box[new_r][new_c]:
                top = False
            if visited[new_r][new_c] == 0 and box[row][col] == box[new_r][new_c]:
                visited[new_r][new_c] = 1
                find_mountain(new_r, new_c)
            else:
                continue
        else:
            continue
    return

N, M = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
result = 0

for r in range(N):
    for c in range(M):
        if box[r][c] != 0 and visited[r][c] == 0:
            top = True
            find_mountain(r, c)
            if top:
                result += 1

print(result)