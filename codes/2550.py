# # 2550.[G3] 전구
# # https://www.acmicpc.net/problem/2550
#
# import sys
# sys.stdin = open('sample.txt', 'r')
#
# N = int(input())
# switch = list(map(int, input().split()))
# bulb = list(map(int, input().split()))
# bulb_index = [0 for _ in range(N)]
# for k in switch:
#     bulb_index[bulb.index(k)] = switch.index(k)
# # print(bulb_index)
# result_cnt = 0
# result_text = ""
# for start in range(N - 1):
#     cnt = 1
#     clicked = [bulb_index[start]]
#     next_index = bulb_index[start]
#     for compare in range(start + 1, N):
#         if next_index < bulb_index[compare]:
#             cnt += 1
#             clicked.append(bulb_index[compare])
#             next_index = bulb_index[compare]
#     if cnt > result_cnt:
#         result_cnt = cnt
#         result_text = ' '.join(list(map(str, clicked)))
#
# result_arr = list(map(int, result_text.split()))
# result = []
# for k in result_arr:
#     result.append(switch[k])
# result.sort()
#
# print(result_cnt)
# print(*result)


# import sys
# sys.stdin = open('sample.txt', 'r')
#
# def find_switch(b, i, c):
#     global result_cnt, result_text
#
#     if i >= N:
#         if c > result_cnt:
#             result_cnt = c
#             result_text = b
#         return
#     bulb_arr = list(map(int, b.split()))
#     if len(bulb_arr) > 0:
#         if bulb_arr[-1] < bulb_index[i]:
#             find_switch(" ".join(map(str, bulb_arr)), i + 1, c)
#             bulb_arr.append(bulb_index[i])
#             find_switch(" ".join(map(str, bulb_arr)), i + 1, c + 1)
#         else:
#             find_switch(" ".join(map(str, bulb_arr)), i + 1, c)
#     else:
#         find_switch("", i + 1, c)
#         find_switch(str(bulb_index[i]), i + 1, c + 1)
#
# N = int(input())
# switch = list(map(int, input().split()))
# bulb = list(map(int, input().split()))
# bulb_index = [0 for _ in range(N)]
# for k in switch:
#     bulb_index[bulb.index(k)] = switch.index(k)
# # print(bulb_index)
# result_cnt = 0
# result_text = ""
# find_switch("", 0, 0)
#
# result_arr = list(map(int, result_text.split()))
# result = []
# for k in result_arr:
#     result.append(switch[k])
# result.sort()
# print(result_cnt)
# print(*result)



# 2550.[G3] 전구
# https://www.acmicpc.net/problem/2550
import sys
N = int(input())
switch = list(map(int, input().split()))
bulb = list(map(int, input().split()))
# 각 전구와 연결된 스위치의 인덱스
switch_index = [0 for _ in range(N)]
for k in switch:
    switch_index[bulb.index(k)] = switch.index(k)
print(switch_index)

