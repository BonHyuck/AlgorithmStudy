'''
2 3 10
10 15 15
13 11 20
'''

import sys

C, D, M = map(int, sys.stdin.readline().split())
stocks = [list(map(int, sys.stdin.readline().split())) for _ in range(C)]
money = [0 for _ in range(500001)]

for d in range(1, D):
    for s in range(C):
        for m in range(stocks[s][d - 1], M + 1):
            money[M] = max(money[m], money[m - stocks[s][d - 1]] + stocks[s][d] - stocks[s][d - 1])
    M += money[M]
print(M)

# N, K = map(int, input().split())
# item = [[0, 0]]
# for i in range(1, N + 1):
#     item.append(list(map(int, input().split())))
# dp = [[0] * (K + 1) for _ in range(N + 1)]
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         if j >= item[i][0]:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1])
#         else:
#             dp[i][j] = dp[i-1][j]
#
# print(dp[N][K])

# import sys
#
# N, D, M = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 날짜별 최대 이익계산
# revenue = []
# day = -1
# while day < D - 2:
#     # 다음꺼 계산
#     day += 1
#     for k in range(N):
#         if arr[k][day + 1] >= arr[k][day]:
#             revenue.append((k, arr[k][day + 1]))
#     revenue = sorted(revenue, key=lambda x: x[1], reverse=True)
#     today_total = 0
#     for k in range(len(revenue)):
#         stock, price = revenue.pop(0)
#         if M >= arr[stock][day]:
#             # 주식 매입
#             M -= arr[stock][day]
#             today_total += price
#     # 오늘 번 돈 더하기
#     M += today_total
#
# print(M)
