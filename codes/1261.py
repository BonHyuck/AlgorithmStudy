# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def find_path(r, c, cnt):
#     global result
#
#     if result < cnt:
#         return
#
#     if r == M - 1 and c == N - 1:
#         if cnt < result:
#             result = cnt
#         return
#
#     visited[r][c] = 1
#     for k in range(4):
#         new_r = r + dx[k]
#         new_c = c + dy[k]
#         if 0 <= new_r < M and 0 <= new_c < N:
#             if visited[new_r][new_c] == 0:
#                 if box[new_r][new_c] == 1:
#                     box[new_r][new_c] = 0
#                     find_path(new_r, new_c, cnt + 1)
#                     box[new_r][new_c] = 1
#                 else:
#                     find_path(new_r, new_c, cnt)
#     visited[r][c] = 0
#
#
#
# N, M = map(int, input().split())
# box = [list(map(int, input())) for _ in range(M)]
# visited = [[0 for _ in range(N)] for _ in range(M)]
# result = float('inf')
# find_path(0, 0, 0)
# print(result)


# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# N, M = map(int, input().split())
# box = [list(map(int, input())) for _ in range(M)]
# visited = [[0 for _ in range(N)] for _ in range(M)]
# distance = [[float('inf') for _ in range(N)] for _ in range(M)]
# distance[0][0] = 0
# queue = [(0, 0)]
#
# while queue:
#     row, col = queue.pop(0)
#     if visited[row][col] == 0:
#         visited[row][col] = 1
#         for k in range(4):
#             cnt = distance[row][col]
#             new_r = row + dx[k]
#             new_c = col + dy[k]
#             if 0 <= new_r < M and 0 <= new_c < N:
#                 if visited[new_r][new_c] == 0:
#                     queue.append((new_r, new_c))
#                     if box[new_r][new_c] == 1:
#                         cnt += 1
#                     distance[new_r][new_c] = min(distance[new_r][new_c], cnt)
#
# print(distance[M-1][N-1])

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
box = [list(map(int, input())) for _ in range(M)]
distance = [[float('inf') for _ in range(N)] for _ in range(M)]
distance[0][0] = 0
queue = deque([(0, 0)])

while queue:
    row, col = queue.popleft()
    for k in range(4):
        new_r = row + dx[k]
        new_c = col + dy[k]
        if 0 <= new_r < M and 0 <= new_c < N:
            if distance[new_r][new_c] == float('inf'):
                if box[new_r][new_c] == 0:
                    queue.appendleft((new_r, new_c))
                    distance[new_r][new_c] = distance[row][col]
                else:
                    queue.append((new_r, new_c))
                    distance[new_r][new_c] = distance[row][col] + 1

print(distance[M-1][N-1])



