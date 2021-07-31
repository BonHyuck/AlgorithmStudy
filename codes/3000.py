# 3000. [G5] 직각 삼각형
# https://www.acmicpc.net/problem/3000

import sys

N = int(sys.stdin.readline())
dict_x = {}
dict_y = {}
points = []
for k in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dict_x[x] = dict_x.get(x, 0) + 1
    dict_y[y] = dict_y.get(y, 0) + 1
    points.append((x, y))

result = 0
for x, y in points:
    result += (dict_x[x] - 1) * (dict_y[y] - 1)
print(result)