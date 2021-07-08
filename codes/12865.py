# 12865. 평범한 배낭
# https://www.acmicpc.net/problem/12865

# def start_select(index, weight, value):
#     global max_value
#
#     if weight > K:
#         return
#
#     if index >= N:
#         if max_value < value:
#             max_value = value
#         return
#     # 해당 인덱스의 물건 선택
#     start_select(index + 1, weight + box[index][0], value + box[index][1])
#     # 선택 안하고 넘어가기
#     start_select(index + 1, weight, value)
#
#     return
#
#
# N, K = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(N)]
# max_value = 0
# start_select(0, 0, 0)
# print(max_value)

N, K = map(int, input().split())
item = [[0, 0]]
for i in range(1, N + 1):
    item.append(list(map(int, input().split())))
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= item[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
