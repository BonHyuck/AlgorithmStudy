# import sys
# from collections import deque
#
# N = int(sys.stdin.readline())
# box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# result_list = deque([])
# for r in range(N):
#     for c in range(N):
#         result_list.append(box[r][c])
#         result_list = deque(sorted(result_list))
#         if len(result_list) > N:
#             result_list.popleft()
# print(result_list[0])

# 2075. [G5] N번째 큰 수
# https://www.acmicpc.net/problem/2075

# import sys
# import heapq
#
# N = int(sys.stdin.readline().rstrip())
# box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# heap = []
# for r in range(N):
#     for c in range(N):
#         heapq.heappush(heap, box[r][c])
#         if len(heap) > N:
#             heapq.heappop(heap)
# print(heap[0])

# 2075. [G5] N번째 큰 수
# https://www.acmicpc.net/problem/2075

N = int(input())
arr = []
for k in range(N):
    arr.extend(list(map(int, input().split())))
    # N번째 큰 수이기 때문에 큰 수가 앞에 오게끔 정렬
    arr.sort(reverse=True)
    # N만큼 끊어주기
    if len(arr) > N:
        arr = arr[0:N]
print(arr[N - 1])

N = int(input())
arr = []
for k in range(N):
    arr.extend(list(map(int, input().split())))

arr.sort(reverse=True)
print(arr[N - 1])