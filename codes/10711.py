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

from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

N, M = map(int, input().split())
castle = [list(input()) for _ in range(N)]
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
    row, col = queue.popleft()
    for k in range(8):
        new_r = row + dx[k]
        new_c = col + dy[k]
        if 0 <= new_r < N and 0 <= new_c < M:
            if castle[new_r][new_c] > 0:
                castle[new_r][new_c] -= 1
                if castle[new_r][new_c] == 0:
                    pado[new_r][new_c] = pado[row][col] + 1
                    queue.append((new_r, new_c))

result = 0
for r in range(N):
    result = max(max(pado[r]), result)
print(result)




