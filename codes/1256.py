def set_dp(row, col):

    if row <= 0 or col <= 0:
        return 1

    if dp[row][col] > 0:
        return dp[row][col]

    dp[row][col] = set_dp(row - 1, col) + set_dp(row, col - 1)

    return dp[row][col]


N, M, K = map(int, input().split())
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
# 단어가 1종류 (a or z)만으로 이뤄져있으면 1개 단어밖에 없음
for c in range(1, M + 1):
    dp[0][c] = 1
for r in range(1, N + 1):
    dp[r][0] = 1
set_dp(N, M)
# print(dp)
if dp[N][M] < K:
    print(-1)
else:
    result = ""
    while True:
        if N == 0:
            result += 'z' * M
            break
        if M == 0:
            result += 'a' * N
            break
        if dp[N - 1][M] >= K:
            result = result + 'a'
            N -= 1
        else:
            result += 'z'
            K -= dp[N - 1][M]
            M -= 1
    print(result)

