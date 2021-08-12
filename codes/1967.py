'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
'''

N = int(input())
tree = [[] for _ in range(N + 1)]

# 트리의 부모, 자식 구분 없이 연결된 노드와 거리 기록
for k in range(N - 1):
    parent, child, dist = map(int, input().split())
    tree[parent].append((child, dist))
    tree[child].append((parent, dist))

# 루트에서 가장 멀리 있는 정점 일단 찾기
first_queue = [1]
# 루트에서 다음 노드(index)까지 거리 표시 배열
dist_arr = [-1 for _ in range(N + 1)]
# 자기 자신은 0
dist_arr[1] = 0
while first_queue:
    node = first_queue.pop(0)
    for next_node, distance in tree[node]:
        if dist_arr[next_node] == -1:
            dist_arr[next_node] = dist_arr[node] + distance
            first_queue.append(next_node)
# 가장 멀리 있는 노드
first = dist_arr.index(max(dist_arr))

# 루트에서 가장 멀리 있는 노드로부터 가장 먼 노드 찾기
second_queue = [first]
dist_arr = [-1 for _ in range(N + 1)]
dist_arr[first] = 0
while second_queue:
    node = second_queue.pop(0)
    for next_node, distance in tree[node]:
        if dist_arr[next_node] == -1:
            dist_arr[next_node] = dist_arr[node] + distance
            second_queue.append(next_node)
result = max(dist_arr)
print(result)




# def find_leaf(node, distance):
#     global result
#     if distance > 0 and leaf[node] == 0:
#         if result < distance:
#             result = distance
#         return
#     for next_node in range(1, N+1):
#         if node != next_node and visited[start_node][next_node] == 0:
#             if tree[node][next_node] > 0:
#                 visited[start_node][next_node] = 1
#                 visited[next_node][start_node] = 1
#                 find_leaf(next_node, distance + tree[node][next_node])
#     return
#
#
# N = int(input())
# tree = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# leaf = [0 for _ in range(N + 1)]
# for k in range(N - 1):
#     parent, child, dist = map(int, input().split())
#     tree[parent][child] = dist
#     tree[child][parent] = dist
#     leaf[parent] = 1
#
# result = 0
#
# visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
#
# for i in range(1, N + 1):
#     if leaf[i] == 0:
#         start_node = i
#         find_leaf(i, 0)
# # for r in range(N+1):
# #     print(r, visited[r])
#
# print(result)





# def find_leaf(node, distance):
#     global result
#     # 거리가 0보다 크며 도달한 노드가 리프노드라면
#     # 끝
#     if distance > 0 and leaf[node] == 0:
#         if result < distance:
#             result = distance
#         return
#
#     # 연결된 다음 노드
#     for next_node in range(1, N + 1):
#         if node != next_node and visited[next_node] == 0:
#             if tree[node][next_node] != 0:
#                 visited[next_node] = 1
#                 find_leaf(next_node, distance + tree[node][next_node])
#                 visited[next_node] = 0
#     return
#
#
#
# N = int(input())
# # 트리 표시
# tree = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# # 리프노드 표시
# leaf = [0 for _ in range(N + 1)]
# # 노드 간의 거리 저장 + 리프 노드 아닌 것 표시
# for k in range(N - 1):
#     parent, child, dist = map(int, input().split())
#     tree[parent][child] = dist
#     tree[child][parent] = dist
#     leaf[parent] = 1
#
# result = 0
#
# # 반복문을 돌면서
# for i in range(1, N + 1):
#     # 리프노드라면
#     if leaf[i] == 0:
#         # 탐색 시작
#         visited = [0 for _ in range(N + 1)]
#         visited[i] = 1
#         find_leaf(i, 0)
#
# print(result)
#
# print(dist_arr)
# print(leaf)