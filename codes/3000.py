# 3000. [G5] 직각 삼각형
# https://www.acmicpc.net/problem/3000

# 직각삼각형의 원리는 간단하다.
# 한 점과 x값이 같은 다른 점과 y값이 같은 다른점
# 이렇게 3개의 점이 직각삼각형을 만든다.

import sys

N = int(sys.stdin.readline())
dict_x = {}
dict_y = {}
points = []
for k in range(N):
    x, y = map(int, sys.stdin.readline().split())
    # 해당 x 좌표를 가진 경우의 수를 센다
    dict_x[x] = dict_x.get(x, 0) + 1
    # 해당 y 좌표를 가진 경우의  수를 센다.
    dict_y[y] = dict_y.get(y, 0) + 1
    points.append((x, y))

result = 0
for x, y in points:
    # 한 점, x 값이 같은 경우 - 1(자기 자신), y 값이 같은 경우 - 1(자기 자신)
    result += (dict_x[x] - 1) * (dict_y[y] - 1)
print(result)