N = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for i in range(N)]
dp[0][arr[0]] = 1
for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if 0 <= j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if 0 <= j - arr[i] <= 20:
                dp[i][j - arr[i]] += dp[i - 1][j]
print(dp[N - 2][arr[-1]])