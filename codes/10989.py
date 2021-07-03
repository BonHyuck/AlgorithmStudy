# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr = sorted(arr)
# for n in arr:
#     print(n)

# N = int(input())
# arr = [0 for _ in range(10001)]
# for k in range(N):
#     num = int(input())
#     arr[num] += 1
# for i in range(10001):
#     if arr[i] != 0:
#         for j in range(arr[i]):
#             print(i)

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001
for k in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1
for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)