import sys
from copy import deepcopy

N, M = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = []
for r in range(N):
    if sum(box[r]) < 0:
        queue.append([("r", r)])

for c in range(M):
    total_col = 0
    for r in range(N):
        total_col += box[r][c]
    if total_col < 0:
        queue.append([("c", c)])

result = -1

while queue:
    possibles = queue.pop(0)
    length = len(possibles)
    if length > 100000:
        break
    cube = deepcopy(box)
    for check, number in possibles:
        # 행 바꾸기
        if check == 'r':
            for c in range(M):
                cube[number][c] *= -1
        # 열 바꾸기
        if check == 'c':
            for r in range(N):
                cube[r][number] *= -1

    next_one = []
    next_one.extend(possibles)
    for r in range(N):
        if sum(cube[r]) < 0:
            next_one.append(("r", r))

    for c in range(M):
        total_col = 0
        for r in range(N):
            total_col += cube[r][c]
        if total_col < 0:
            next_one.append(("c", c))

    if len(next_one) != length:
        queue.append(next_one)
    else:
        result = length
        break
print(result)

# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# letter = ''
# number = -1
# minimum = 0
# result = 0
# while True:
#     if result > 20*20:
#         result = -1
#         break
#     # 행
#     for r in range(N):
#         if sum(box[r]) < minimum:
#             letter = 'r'
#             number = r
#             minimum = sum(box[r])
#     # 열
#     for c in range(M):
#         total_col = 0
#         for r in range(N):
#             total_col += box[r][c]
#         if total_col < minimum:
#             letter = "c"
#             number = c
#             minimum = total_col
#
#     # 바꾸기
#     if letter == "r":
#         for c in range(M):
#             box[number][c] *= -1
#     elif letter == "c":
#         for r in range(N):
#             box[r][number] *= -1
#     else:
#         break
#
#     letter = ""
#     number = -1
#     minimum = 0
#     result += 1
#
# print(result)

