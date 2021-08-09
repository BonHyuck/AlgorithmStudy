while True:
    N, M = map(float, input().split())
    N = int(N)
    M = int(M * 100 + 0.5)
    if N == 0 and M == 0:
        break
    dp = [0 for _ in range(10001)]
    candies = []
    for k in range(N):
        C, P = map(float, input().split())
        C = int(C)
        P = int(P * 100 + 0.5)
        candies.append((C, P))

    for money in range(1, M + 1):
        for calories, price in candies:
            # 쓸 수 있는 돈보다 가격이 더 높음
            if money - price < 0:
                continue
            # 해당 돈에서 최대 칼로리
            dp[money] = max(dp[money], dp[money - price] + calories)

    print(dp[M])