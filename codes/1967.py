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

def find_leaf(node, distance):
    global result
    if distance > 0 and leaf[node] == 0:
        if result < distance:
            result = distance
        return

    for next_node in range(1, N + 1):
        if node != next_node and visited[next_node] == 0:

            if tree[node][next_node] != 0:
                visited[next_node] = 1
                find_leaf(next_node, distance + tree[node][next_node])
                visited[next_node] = 0
    return



N = int(input())
tree = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
leaf = [0 for _ in range(N + 1)]
for k in range(N - 1):
    parent, child, dist = map(int, input().split())
    tree[parent][child] = dist
    tree[child][parent] = dist
    leaf[parent] = 1

result = 0

for i in range(1, N + 1):
    if leaf[i] == 0:
        visited = [0 for _ in range(N + 1)]
        visited[i] = 1
        find_leaf(i, 0)

print(result)

# print(dist_arr)
# print(leaf)