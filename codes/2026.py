K, N, F = map(int,input().split())
arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for k in range(F):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1

friends_cnt = [0 for _ in range(N + 1)]
possible = 0
for r in range(1, N + 1):
    friends_cnt[r] = arr[r].count(1)
    if friends_cnt[r] >= K - 1:
        possible += 1
if possible < K:
    print(-1)
else:
    print(friends_cnt)