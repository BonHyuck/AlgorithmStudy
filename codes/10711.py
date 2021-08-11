# from collections import deque
#
# dx = [-1, 1, 0, 0, -1, -1, 1, 1]
# dy = [0, 0, -1, 1, -1, 1, -1, 1]
#
# def break_castle():
#     for r in range(N):
#         for c in range(M):
#             if castle[r][c] != '.':
#                 sand = int(castle[r][c])
#                 # 모래가 없는 곳
#                 no_sand = 0
#                 for k in range(8):
#                     new_r = r + dx[k]
#                     new_c = c + dy[k]
#                     if 0 <= new_r < N and 0 <= new_c < M:
#                         if castle[new_r][new_c] == '.':
#                             no_sand += 1
#                 if no_sand >= sand:
#                     queue.append((r, c))
#     return
#
# N, M = map(int, input().split())
# castle = [list(input()) for _ in range(N)]
# result = 0
# while True:
#     # 없어질 칸의 좌표
#     queue = deque()
#
#     break_castle()
#
#     if len(queue) == 0:
#         break
#
#     result += 1
#     while queue:
#         row, col = queue.popleft()
#         castle[row][col] = "."
# print(result)

# dx = [-1, 1, 0, 0, -1, -1, 1, 1]
# dy = [0, 0, -1, 1, -1, 1, -1, 1]
#
# N, M = map(int, input().split())
# castle = [list(input()) for _ in range(N)]
# result = 0
# sand_queue = []
# for r in range(N):
#     for c in range(M):
#         if castle[r][c] != ".":
#             sand_queue.append((r, c, int(castle[r][c])))
#
# while True:
#     no_queue = []
#     for i in range(len(sand_queue)):
#         row, col, sand = sand_queue.pop(0)
#         no_sand = 0
#         for k in range(8):
#             new_r = row + dx[k]
#             new_c = col + dy[k]
#             if 0 <= new_r < N and 0 <= new_c < M:
#                 if castle[new_r][new_c] == ".":
#                     no_sand += 1
#         if no_sand >= sand:
#             no_queue.append((row, col))
#         else:
#             sand_queue.append((row, col, sand))
#
#     if len(no_queue) == 0:
#         break
#     result += 1
#     while no_queue:
#         r, c = no_queue.pop()
#         castle[r][c] = '.'
#
# print(result)

# 10711.[G3] 모래성
# https://www.acmicpc.net/problem/10711

# 처음엔 모래성을 기준으로 무너져내리는 것을 전부 확인했었다.
# 물론 시간초과가 떴으니 해당 방법으로 풀 수 없었다.
# 모래성은 1이든 9든 살아있는건 똑같다.
# 모래성이 기준이 아닌 파도가 들어오는 부분을 기준으로 카운팅을 했다.

from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

N, M = map(int, input().split())
# 모래성
castle = [list(input()) for _ in range(N)]
# 해당 모래성이 언제쯤 없어지는지
pado = [[0 for _ in range(M)] for _ in range(N)]
queue = deque()
for r in range(N):
    for c in range(M):
        if castle[r][c] == ".":
            queue.append((r, c))
            castle[r][c] = 0
        else:
            castle[r][c] = int(castle[r][c])


while queue:
    # 파도가 들어온다.
    row, col = queue.popleft()
    # 8방향 확인
    for k in range(8):
        new_r = row + dx[k]
        new_c = col + dy[k]
        if 0 <= new_r < N and 0 <= new_c < M:
            # 해당 방향에 모래성이 있으면
            if castle[new_r][new_c] > 0:
                # 1번 건드린다.
                castle[new_r][new_c] -= 1
                # 위로 인해 무너졌다면
                if castle[new_r][new_c] == 0:
                    # 얼마만에 무너진건지 세준다.
                    # 이전 모래성이 무너져서 생긴 파도일수 있으니
                    # 이전 파도에서 1을 더해준다.
                    pado[new_r][new_c] = pado[row][col] + 1
                    # 새로 파도가 칠 부분이니 추가
                    queue.append((new_r, new_c))

result = 0
# 최대값이 답이다.
for r in range(N):
    result = max(max(pado[r]), result)
print(result)




