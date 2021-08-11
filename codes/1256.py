def set_dp(row, col):

    if row <= 0 or col <= 0:
        return 1

    if dp[row][col] > 0:
        return dp[row][col]
    # row, col의 자리는 row - 1, col의 단어에서 a를 더해주는 것과
    # row, col - 1의 단어에서 z를 더해주는 것과 같음
    dp[row][col] = set_dp(row - 1, col) + set_dp(row, col - 1)

    return dp[row][col]


N, M, K = map(int, input().split())
# r = a의 개수, c = z의 개수
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
# 단어가 1종류 (a or z)만으로 이뤄져있으면 1개 단어밖에 없음
for c in range(1, M + 1):
    dp[0][c] = 1
for r in range(1, N + 1):
    dp[r][0] = 1
# DP 배열 세팅
set_dp(N, M)
# print(dp)
# N개의 a와 M개의 z를 붙였음에도 K번쨰 단어는 없음
if dp[N][M] < K:
    print(-1)
# 그렇지 않다면
else:
    result = ""
    while True:
        # a가 없으면 남은 M만큼 z만 붙여주고
        if N == 0:
            result += 'z' * M
            break
        # z가 없으면 남은 N만큼 a만 붙여준다.
        if M == 0:
            result += 'a' * N
            break
        # a가 1개 없는 단어의 수가 K보다 크거나 같으면
        # a를 뒤에 붙여서 새로운 단어를 만들어낼 수 있다.
        # a를 뒤에 붙여서 만든 단어는 굳이 z를 붙이는 경우를
        # 확인하지 않아도 K번째가 될 수 있다.
        if dp[N - 1][M] >= K:
            result = result + 'a'
            N -= 1
        else:
            result += 'z'
            K -= dp[N - 1][M]
            M -= 1
    print(result)

