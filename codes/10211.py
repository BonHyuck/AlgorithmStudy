# 10211. Maximum Subarray(S3)
# https://www.acmicpc.net/problem/10211

T = int(input())
for test_case in range(1, T+1):
    # 입력값
    N = int(input())
    # 입력 배열
    arr = list(map(int, input().split()))
    # 누적합
    dp = [0 for _ in range(N)]
    dp[0] = arr[0]
    # 누적합과 현재 배열의 값을 비교해서 최대값을 입력
    for k in range(1, N):
        dp[k] = max(arr[k], dp[k-1] + arr[k])
    print(max(dp))