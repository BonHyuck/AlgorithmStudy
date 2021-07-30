# 2636. 치즈
# https://www.acmicpc.net/problem/2636

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_open():
    # 시작점
    queue = [(0, 0)]
    # 방문처리
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    while queue:
        row, col = queue.pop(0)
        for k in range(4):
            new_r = row + dx[k]
            new_c = col + dy[k]
            if 0 <= new_r < N and 0 <= new_c < M:
                if visited[new_r][new_c] == 0 and box[new_r][new_c] == 0:
                    visited[new_r][new_c] = 1
                    queue.append((new_r, new_c))
                    # 닿아있는 부분 공기넣기
                    open_area[new_r][new_c] = 0


N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
# 비어있음 여부 확인 배열
# 0 : 공기, 1: 공기 아님
open_area = [[1 for _ in range(M)] for _ in range(N)]
# 가장자리 비워두기
for c in range(M):
    open_area[0][c] = 0
    open_area[N - 1][c] = 0
for r in range(N):
    open_area[r][0] = 0
    open_area[r][M - 1] = 0

cheese_count = []
time = 0

while True:
    # 치즈가 전부 녹았는지 확인
    count_zero = 0
    for r in range(N):
        count_zero += box[r].count(0)
    if count_zero == N*M:
        break

    # 열린 부분 표시하기
    find_open()

    # 열린 부분과 닿아있는 치즈 찾기
    queue = []
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:
                for k in range(4):
                    new_r = r + dx[k]
                    new_c = c + dy[k]
                    if 0 <= new_r < N and 0 <= new_c < M:
                        if box[new_r][new_c] == 0 and open_area[new_r][new_c] == 0:
                            queue.append((r, c))
                            break

    if len(queue) > 0:
        cheese_count.append(len(queue))
        time += 1

    while queue:
        row, col = queue.pop(0)
        box[row][col] = 0

print(time)
print(cheese_count[-1])



