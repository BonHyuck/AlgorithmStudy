TC = 1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while True:
    N = int(input())
    if N == 0:
        break
    box = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf') for _ in range(N)] for _ in range(N)]
    dp[0][0] = box[0][0]
    queue = [(0, 0)]
    while queue:
        row, col = queue.pop(0)
        for k in range(4):
            new_r = row + dr[k]
            new_c = col + dc[k]
            if 0 <= new_r < N and 0 <= new_c < N:
                if dp[row][col] + box[new_r][new_c] < dp[new_r][new_c]:
                    queue.append((new_r, new_c))
                    dp[new_r][new_c] = dp[row][col] + box[new_r][new_c]
    print("Problem {}: {}".format(TC, dp[N-1][N-1]))
    TC += 1