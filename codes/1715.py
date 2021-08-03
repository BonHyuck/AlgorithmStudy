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


# 1715. [G4] 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import heapq

N = int(input())
arr = []
for _ in range(N):
    heapq.heappush(arr, int(input()))

# 1개일 경우 비교 없음
if len(arr) == 1:
    print(0)
else:
    answer = 0
    while len(arr) > 1:  # 1개일 경우 비교하지 않아도 된다
        # 제일 작은거
        first = heapq.heappop(arr)
        # 다음 작은거
        second = heapq.heappop(arr)
        # 비교 마침
        answer += first + second
        # 다시 넣어서 최소 연산
        heapq.heappush(arr, first + second)

    print(answer)
