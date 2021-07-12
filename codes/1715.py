# import sys
#
# N = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(N)]
# arr = sorted(arr)
# for k in range(1, N):
#     arr[k] = arr[k] + arr[k-1]
#
# print(sum(arr) - arr[0])

# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr = sorted(arr)
# result = []
# while len(arr) > 1:
#     first = arr.pop(0)
#     second = arr.pop(0)
#     arr.append(first + second)
#     result.append(first + second)
#     arr.sort()
# print(sum(result))

import heapq
import sys

N = int(input())
card_deck = []
for _ in range(N):
    heapq.heappush(card_deck, int(sys.stdin.readline()))

if len(card_deck) == 1:  # 1개일 경우 비교하지 않아도 된다
    print(0)
else:
    answer = 0
    while len(card_deck) > 1:  # 1개일 경우 비교하지 않아도 된다
        temp_1 = heapq.heappop(card_deck)  # 제일 작은 덱
        temp_2 = heapq.heappop(card_deck)  # 두번째로 작은 덱
        answer += temp_1 + temp_2  # 현재 비교 횟수를 더해줌
        heapq.heappush(card_deck, temp_1 + temp_2)  # 더한 덱을 다시 넣어줌

    print(answer)
