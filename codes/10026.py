dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_blind(row, col):
    queue = [(row, col)]
    color = box[row][col]
    visited[row][col] = 1

    while queue:
        r, c = queue.pop(0)

        for k in range(4):
            new_r = r + dr[k]
            new_c = c + dc[k]
            if 0 <= new_r < N and 0 <= new_c < N:
                if visited[new_r][new_c] == 0:

                    if box[new_r][new_c] == color:
                        visited[new_r][new_c] = 1
                        queue.append((new_r, new_c))
                    else:
                        if color == "R" and box[new_r][new_c] == "G":
                            visited[new_r][new_c] = 1
                            queue.append((new_r, new_c))
                        elif color == "G" and box[new_r][new_c] == "R":
                            visited[new_r][new_c] = 1
                            queue.append((new_r, new_c))
    return 1


def find_not_blind(row, col):
    queue = [(row, col)]
    color = box[row][col]
    visited_not[row][col] = 1

    while queue:
        r, c = queue.pop(0)

        for k in range(4):
            new_r = r + dr[k]
            new_c = c + dc[k]
            if 0 <= new_r < N and 0 <= new_c < N:
                if visited_not[new_r][new_c] == 0 and box[new_r][new_c] == color:
                    visited_not[new_r][new_c] = 1
                    queue.append((new_r, new_c))
    return 1


N = int(input())
box = [list(input()) for _ in range(N)]

visited = [[0 for _ in range(N)] for _ in range(N)]
visited_not = [[0 for _ in range(N)] for _ in range(N)]
result = 0
result_not = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            result += find_blind(r, c)
        if visited_not[r][c] == 0:
            result_not += find_not_blind(r, c)
print(result_not, result)