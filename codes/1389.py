# def find_connection(row):
#     queue = []
#     temp = []
#     visited = [0 for _ in range(N + 1)]
#     for k in range(1, N+1):
#         if connections[row][k] == 1:
#             temp.append(k)
#             visited[k] = 1
#     if len(temp) > 0:
#         queue.append(temp)
#     else:
#         return
#
#     steps = 1
#
#
#     while connections[row].count(0) > 1:
#         people = queue.pop(0)
#         temp = []
#         steps += 1
#         for person in people:
#             for i in range(1, N+1):
#                 if i != person and connections[person][i] != 0 and visited[i] == 0:
#                     temp.append(i)
#                     visited[i] = 1
#                     connections[row][i] = steps
#                     connections[i][row] = steps
#         if len(temp) == 0:
#             return
#         else:
#             queue.append(temp)
#
# N, M = map(int, input().split())
# connections = [[0 for _ in range(N+1)] for _ in range(N+1)]
# for k in range(M):
#     x, y = map(int, input().split())
#     connections[x][y] = 1
#     connections[y][x] = 1
#
# for r in range(N):
#     if connections[r].count(0) > 1:
#         find_connection(r)
#
# result_value = 9876543210
# result_index = 0
#
# for j in range(1, N+1):
#     if sum(connections[j]) < result_value:
#         result_value = sum(connections[j])
#         result_index = j
# print(result_index)


# def find_connection(row):
#     queue = []
#     temp = []
#     visited = [0 for _ in range(N + 1)]
#     visited[row] = 1
#     for k in range(1, N+1):
#         if connections[row][k] == 1:
#             temp.append(k)
#             visited[k] = 1
#     if len(temp) > 0:
#         queue.append(temp)
#     else:
#         return
#
#     steps = 1
#
#
#     while connections[row].count(float('inf')) > 1:
#         people = queue.pop(0)
#         temp = []
#         steps += 1
#         for person in people:
#             for i in range(1, N+1):
#                 if i != person and connections[person][i] != float('inf') and visited[i] == 0:
#                     temp.append(i)
#                     visited[i] = 1
#                     connections[row][i] = min(steps, connections[row][i])
#                     connections[i][row] = min(steps, connections[i][row])
#         if len(temp) == 0:
#             return
#         else:
#             queue.append(temp)
#
#
# N, M = map(int, input().split())
# connections = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
# for k in range(M):
#     x, y = map(int, input().split())
#     connections[x][y] = 1
#     connections[y][x] = 1
#
# for r in range(N):
#     if connections[r].count(float('inf')) > 1:
#         find_connection(r)
# # print(connections)
# result_value = 9876543210
# result_index = 0
#
# for r in range(1, N+1):
#     total = 0
#     for c in range(1, N+1):
#         if connections[r][c] != float('inf'):
#             total += connections[r][c]
#     if total < result_value:
#         result_value = total
#         result_index = r
# print(result_index)

# 1389. ?????? ???????????? 6?????? ??????
# https://www.acmicpc.net/problem/1389

def find_kevin(start):
    # ?????? ???
    queue = [start]
    # ?????? ???????????? ?????? ??????(?????????)????????? ?????? ????????? ??? ?????????
    cnt = [-1 for _ in range(N+1)]
    # ????????? 0
    cnt[start] = 0
    while queue:
        number = queue.pop(0)
        # arr[number] = number??? 1????????? ????????? ?????? ??????
        # next_number = number??? 1????????? ????????? ???
        for next_number in arr[number]:
            # ?????? ????????? ????????????
            if cnt[next_number] == -1:
                # ????????? ???????????? ?????? queue??? ??????
                queue.append(next_number)
                # 1?????? ??????????????? +1
                cnt[next_number] = cnt[number] + 1
    # ?????? ?????? ??? ?????? ????????? ?????? ??? +1 (index = 0 ?????? -1 ??????)
    result[start] = sum(cnt) + 1

# ?????????
N, M = map(int, input().split())
# ?????? ????????? ?????? ??????
# ????????? -> ?????? ?????????
arr = [[] for _ in range(N+1)]
# ??? ???????????? ?????? ?????? ????????? ?????? ?????? ??????
result = [0 for _ in range(N+1)]

# ???????????? ????????? ?????? ????????? ?????? ??????
for k in range(M):
    r, c = map(int, input().split())
    arr[r].append(c)
    arr[c].append(r)

# ?????? ????????? ?????? ?????? ??????
for i in range(1, N+1):
    find_kevin(i)

# ???????????? ?????? ?????? ?????????
result_value = 9876543210
result_index = 0

for j in range(1, N+1):
    if result_value > result[j]:
        result_index = j
        result_value = result[j]

print(result_index)


