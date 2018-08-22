dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_baechu(row, col):
    queue = [(row, col)]

    while queue:
        r, c = queue.pop(0)
        for k in range(4):
            new_r = r + dr[k]
            new_c = c + dc[k]
            if 0 <= new_r < N and 0 <= new_c < M:
                if box[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                    visited[new_r][new_c] = 1
                    queue.append((new_r, new_c))
    return

T = int(input())
for test_case in range(1, T+1):
    M, N, K = map(int, input().split())
    box = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        c, r = map(int, input().split())
        box[r][c] = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1 and visited[r][c] == 0:
                answer += 1
                visited[r][c] = 1
                find_baechu(r, c)

    print(answer)