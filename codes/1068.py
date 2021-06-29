# N = int(input())
# tree = list(map(int, input().split()))
# delete_node = int(input())
# leaves = [1 for _ in range(N)]
# for node in tree:
#     if node > -1:
#         leaves[node] = 0
#
# leaves[delete_node] = 0
#
# for leaf_index in range(N):
#     if leaves[leaf_index] == 1:
#         parent_index = tree[leaf_index]
#         while parent_index > -1:
#             if delete_node == parent_index:
#                 leaves[leaf_index] = 0
#                 break
#             parent_index = tree[parent_index]
#
# print(leaves.count(1))
# 지운 이후 자식이 없어진 부모가 있을 수 있다 => 해당 부모가 리프 노드가 된다.
#
# def find_leaf(idx):
#     global result
#
#     is_leaf = True
#
#     for k in range(N):
#         if tree[idx][k] == 1:
#             is_leaf = False
#             find_leaf(k)
#
#     if is_leaf:
#         result += 1
#
#     return
#
#
# N = int(input())
# parent_nodes = list(map(int, input().split()))
# delete_node = int(input())
# tree = [[0 for _ in range(N)] for _ in range(N)]
# for i in range(N):
#     if i != delete_node and parent_nodes[i] > -1 and parent_nodes[i] != delete_node:
#         tree[parent_nodes[i]][i] = 1
#
# result = 0
# if delete_node != 0:
#     find_leaf(0)
# print(result)

# N = int(input())
# parent_nodes = list(map(int, input().split()))
# delete_node = int(input())
# tree = [[] for _ in range(N)]
# for i in range(N):
#     if i != delete_node and parent_nodes[i] != delete_node and parent_nodes[i] > -1:
#         tree[parent_nodes[i]].append(i)
#
# result = 0
#
# if delete_node == 0:
#     print(result)
# else:
#     queue = [0]
#     while queue:
#         node = queue.pop(0)
#         if len(tree[node]) == 0:
#             result += 1
#         else:
#             queue.extend(tree[node])
#     print(result)

N = int(input())
parent_nodes = list(map(int, input().split()))
delete_node = int(input())
tree = {}
for i in range(N):
    if delete_node == i or parent_nodes[i] == delete_node:
        continue
    if parent_nodes[i] in tree:
        tree[parent_nodes[i]].append(i)
    else:
        tree[parent_nodes[i]] = [i]

result = 0

queue = []

if -1 in tree:
    queue.append(-1)
while queue:
    node = queue.pop()
    if node in tree:
        queue.extend(tree[node])
    else:
        result += 1
print(result)


