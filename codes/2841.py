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
# # 1번 줄부터 6번 줄까지 있음
# guitar = [[] for _ in range(7)]
# result = 0
#
# # 연주해야되는 줄 만큼 반복
# while melody:
#     # 줄(1~6), 프렛
#     row, number = melody.pop(0)
#     # 해당 줄을 연주한 적이 없음
#     # 바로 하나 추가하고 넘어가기
#     if len(guitar[row]) == 0:
#         result += 1
#         guitar[row].append(number)
#         continue
#     # 이미 연주 가능
#     # 바로 넘어가기
#     if number == guitar[row][-1]:
#         continue
#     # 맨 끝에 있는 프렛보다 큰 프렛
#     # 바로 하나 추가하고 넘어가기
#     if number > guitar[row][-1]:
#         guitar[row].append(number)
#         result += 1
#     # 맨 끝에 있는 프렛보다 작은 프렛
#     else:
#         # 현재 연주해야 하는 프렛보다 큰 프렛에서는 손을 떼야함
#         while len(guitar[row]) > 0 and number < guitar[row][-1]:
#             guitar[row].pop()
#             result += 1
#         # 손을 떼고 나니 이미 해당 프렛에 손가락이 있음
#         if len(guitar[row]) > 0 and guitar[row][-1] == number:
#             continue
#         # 아니라면 손을 올리고 넘어가기
#         guitar[row].append(number)
#         result += 1
#
# print(result)

# 2841. [S1] 외계인의 기타 연주
# https://www.acmicpc.net/problem/2841

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