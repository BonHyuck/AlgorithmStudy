T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0 for _ in range(N)]
    dp[0] = arr[0]
    for k in range(1, N):
        dp[k] = max(arr[k], dp[k-1] + arr[i])
    print(max(dp))