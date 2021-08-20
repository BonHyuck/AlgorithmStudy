# N, M = map(int, input().split())
# tree = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# queue = []
# for k in range(M):
#     A, B = map(int, input().split())
#     tree[A][B] = 1
#     queue.append(A)
# queue.sort()
# check = [0 for _ in range(N + 1)]
# result = []
# while queue:
#     prob = queue.pop(0)
#     check[prob] = 1
#     result.append(prob)
#     for next_prob in range(1,  N + 1):
#         if check[next_prob] == 0 and tree[prob][next_prob] == 1:
#             queue.append(next_prob)
#             break
#     queue.sort()
#
# print(" ".join(map(str, result)))

'''
4 2
4 2
3 1

4 4
4 1
1 3
1 2
4 2

'''
import heapq

N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
steps = [0 for _ in range(N + 1)]
for k in range(M):
    A, B = map(int, input().split())
    tree[A].append(B)
    steps[B] += 1

queue = []
for k in range(1, N + 1):
    if steps[k] == 0:
        heapq.heappush(queue, k)

while queue:
    node = heapq.heappop(queue)
    print(node, end=" ")

    for k in range(len(tree[node])):
        next_node = tree[node][k]
        steps[next_node] -= 1
        if steps[next_node] == 0:
            heapq.heappush(queue,  next_node)
