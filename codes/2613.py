"""
8 3
5 4 2 6 9 3 8 7

반례
9 4
9 1 1 1 1 1 1 1 1
"""

# 2613. [G2] 숫자 구슬
# https://www.acmicpc.net/problem/2613

# 이분탐색이라길래 앞의 1477. 휴게소 세우기 문제와 비슷하게 시작했다.
# 구슬의 합을 정해두고 몇개의 그룹으로 나눌 수 있는지 확인하는 방식으로 진행했다.

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 최소 = 1개의 구슬도 1개의 그룹이니
# 아무리 쪼개져도 구슬 1개의 값보다 작아질수 없다.
left = max(arr)
# 최대 = 문제에 나온 조건
right = 100 * N
# 최소값을 구해야하므로 높게 잡았다.
result = float('inf')

# 이분탐색 시작
while left <= right:
    mid = (left + right) // 2
    total = 0
    group = 0
    flag = False
    # 구슬 전체 검사
    for k in range(N):
        # 구슬 자체가 정해둔 값보다 크면
        # 그룹의 최대값은 정해둔 값이 될 수 없다.
        if arr[k] > mid:
            # 기준 변경
            left = mid + 1
            # 추후 넘어가기 위한 변수 변경
            flag = True
            # 반복 끝
            break
        # 그게 아니라면 그룹에 구슬을 더해준다.
        total += arr[k]
        # k번째 구슬이 더해진 총합이 앞서 정해둔 값보다 크면
        # 해당 구슬은 그룹에 더해질 수 없다.
        if total > mid:
            # 그룹에 구슬 더하기 끝 = 그룹이 1개 만들어짐
            group += 1
            # 다음 그룹은 k번째 구슬로 시작
            total = arr[k]
    # 위의 반복문이 중단됐거나
    # 그룹이 기준보다 많으면 최대값의 최소값을 늘려준다.
    if group >= M or flag:
        left = mid + 1
    # 그룹이 적다면 최대값의 최소값을 줄여서 그룹을 더 만들어야된다.
    else:
        right = mid - 1
        # 일단 지금까지의 결과값보다 작으면
        if mid < result:
            # 결과값 저장
            result = mid
print(result)

# 최대값의 최소값은 구했으니 각 그룹에 몇개가 있는지 구한다.
groups = []
cnt = 0
total = 0
# 기준에 맞게 그룹을 나눠준다.
for k in range(N):
    total += arr[k]
    cnt += 1
    if total > result:
        total = arr[k]
        groups.append(cnt - 1)
        cnt = 1
groups.append(cnt)
print(*groups)

# 여기까지만 하면 되는 줄 알고 제출했더니 틀렸다...
"""
반례:
9 4
9 1 1 1 1 1 1 1 1
"""

# 위까지만 진행하면 1 8 로 나온다.
# 구슬 1개, 구슬 8개의 그룹으로 최대값의 최소값은 만족하지만
# 그룹 개수는 틀렸다.
# 아래의 작업을 통해 그룹을 쪼개줘야한다.
# group_diff = 더 필요한 그룹 개수
group_diff = M - len(groups)

for i in range(len(groups)):
    # 그룹에 구슬이 1개면 더 쪼갤수 없다.
    if groups[i] == 1:
        print(groups[i], end=" ")
    else:
        # group_diff 가 없어지거나 1개가 남을때까지 쪼개본다
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


