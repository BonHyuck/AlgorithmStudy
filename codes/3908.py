numbers = [0 for k in range(1121)]
for k in range(2, 557):
    if numbers[k] == 0:
        for i in range(k * 2, 1121, k):
            numbers[i] = 1

primes = []
for k in range(2, len(numbers)):
    if numbers[k] == 0:
        primes.append(k)

dp = [[0 for _ in range(15)] for _ in range(1121)]
dp[0][0] = 1
for i in range(len(primes)):
    for j in range(1120, primes[i] - 1, -1):
        for k in range(1, 15):
            dp[j][k] += dp[j - primes[i]][k-1]

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    print(dp[N][K])