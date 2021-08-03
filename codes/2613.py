"""
8 3
5 4 2 6 9 3 8 7

반례
9 4
9 1 1 1 1 1 1 1 1
"""
N, M = map(int, input().split())
arr = list(map(int, input().split()))

left = max(arr)
right = 100 * N
result = float('inf')

while left <= right:
    mid = (left + right) // 2
    total = 0
    group = 0
    flag = False
    for k in range(N):
        if arr[k] > mid:
            left = mid + 1
            flag = True
            break
        total += arr[k]
        if total > mid:
            group += 1
            total = arr[k]
    if group >= M or flag:
        left = mid + 1
    else:
        right = mid - 1
        if mid < result:
            result = mid
print(result)

groups = []
cnt = 0
total = 0
for k in range(N):
    total += arr[k]
    cnt += 1
    if total > result:
        total = arr[k]
        groups.append(cnt - 1)
        cnt = 1

groups.append(cnt)
group_diff = M - len(groups)

for i in range(len(groups)):
    if groups[i] == 1:
        print(groups[i], end=" ")
    else:
        while groups[i] >= 2 and group_diff >= 1:
            print("1", end=" ")
            groups[i] -= 1
            group_diff -= 1
        print(groups[i], end=" ")




# from itertools import combinations
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# cumulative_total = [0 for _ in range(N)]
# cumulative_total[0] = arr[0]
# for i in range(1, N):
#     cumulative_total[i] = cumulative_total[i-1] + arr[i]
#
# result = float('inf')
# index_possible = list(combinations([i for i in range(N - 1)], M))
#
# for index_arr in index_possible:
#     groups = [0 for _ in range(M)]
#     groups[0] = cumulative_total[index_arr[0]]
#     for k in range(1, len(index_arr)):
#         groups[k] = cumulative_total[index_arr[k]] - cumulative_total[index_arr[k - 1]]
#         if k == len(index_arr) - 1:
#             groups[k] = cumulative_total[-1] - cumulative_total[index_arr[k - 1]]
#
#     result = min(max(groups), result)
# print(result)


