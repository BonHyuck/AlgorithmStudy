'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, K = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
virus = [[] for _ in range(K)]
for r in range(N):
    for c in range(N):
        if box[r][c] != 0:
            virus[box[r][c] - 1].append([r, c])
while S:
    for i in range(K):
        queue = virus[i]
        temp = []
        while queue:
            r, c = queue.pop(0)
            for k in range(4):
                new_r = r + dr[k]
                new_c = c + dc[k]
                if 0 <= new_r < N and 0 <= new_c < N and box[new_r][new_c] == 0:
                    box[new_r][new_c] = i + 1
                    temp.append([new_r, new_c])
        if temp:
            queue.extend(temp)

    S -= 1
print(box[X - 1][Y - 1])
