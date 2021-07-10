# import sys
#
# N, P = map(int, sys.stdin.readline().split())
# guitar = [[0 for _ in range(P+1)] for _ in range(7)]
# melody = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# result = 0
#
# while melody:
#     row, col = melody.pop(0)
#     if guitar[row][col] == 0:
#         result += 1
#         guitar[row][col] = 1
#         for k in range(col+1, P+1):
#             if guitar[row][k] == 1:
#                 guitar[row][k] = 0
#                 result += 1
#
# print(result)

# N, P = map(int, input().split())
# melody = [tuple(map(int, input().split())) for _ in range(N)]
# guitar = [[] for _ in range(7)]
# result = 0
#
# while melody:
#     row, number = melody.pop(0)
#     if len(guitar[row]) == 0:
#         result += 1
#         guitar[row].append(number)
#         continue
#     if number == guitar[row][-1]:
#         continue
#     if number > guitar[row][-1]:
#         guitar[row].append(number)
#         result += 1
#     else:
#         while len(guitar[row]) > 0 and number < guitar[row][-1]:
#             guitar[row].pop()
#             result += 1
#         if len(guitar[row]) > 0 and guitar[row][-1] == number:
#             continue
#         guitar[row].append(number)
#         result += 1
#
# print(result)

import sys

N, P = map(int, sys.stdin.readline().split())
melody = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
guitar = [[] for _ in range(7)]
result = 0

for row, number in melody:
    if len(guitar[row]) == 0:
        result += 1
        guitar[row].append(number)
        continue
    if number == guitar[row][-1]:
        continue
    if number > guitar[row][-1]:
        guitar[row].append(number)
        result += 1
    else:
        while len(guitar[row]) > 0 and number < guitar[row][-1]:
            guitar[row].pop()
            result += 1
        if len(guitar[row]) > 0 and guitar[row][-1] == number:
            continue
        guitar[row].append(number)
        result += 1

print(result)