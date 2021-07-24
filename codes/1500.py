# 1500. [S1] 최대 곱
# https://www.acmicpc.net/problem/1500

N, K = map(int, input().split())
value = N // K
rest = N % K
result = 1
for k in range(rest):
    result *= (value + 1)
for j in range(K - rest):
    result *= value

print(result)