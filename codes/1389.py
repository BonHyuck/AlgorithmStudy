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

# 1389. 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

def find_kevin(start):
    # 시작 값
    queue = [start]
    # 시작 노드에서 다음 노드(인덱스)까지의 케빈 베이컨 수 구하기
    cnt = [-1 for _ in range(N+1)]
    # 본인은 0
    cnt[start] = 0
    while queue:
        number = queue.pop(0)
        # arr[number] = number와 1단계로 연결된 수의 배열
        # next_number = number와 1단계로 연결된 수
        for next_number in arr[number]:
            # 아직 연결이 안돼있음
            if cnt[next_number] == -1:
                # 다음에 확인하기 위해 queue에 넣기
                queue.append(next_number)
                # 1단계 연결이므로 +1
                cnt[next_number] = cnt[number] + 1
    # 결과 값은 각 케빈 베이컨 수의 합 +1 (index = 0 일떄 -1 처리)
    result[start] = sum(cnt) + 1

# 입력값
N, M = map(int, input().split())
# 바로 연결된 노드 표현
# 인덱스 -> 다음 인덱스
arr = [[] for _ in range(N+1)]
# 각 인덱스에 따른 케인 베이컨 수를 담을 배열
result = [0 for _ in range(N+1)]

# 입력값을 받아서 바로 연결된 노드 설정
for k in range(M):
    r, c = map(int, input().split())
    arr[r].append(c)
    arr[c].append(r)

# 모든 노드에 대해 함수 실행
for i in range(1, N+1):
    find_kevin(i)

# 최소값과 그에 따른 인덱스
result_value = 9876543210
result_index = 0

for j in range(1, N+1):
    if result_value > result[j]:
        result_index = j
        result_value = result[j]

print(result_index)


