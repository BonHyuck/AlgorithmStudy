# 1477.  [G4] 휴게소 세우기
# https://www.acmicpc.net/problem/1477

# N, M, L = map(int, input().split())
# road = [0]
# road.extend(list(map(int, input().split())))
# road.append(L)
# road = sorted(road)
# diff = []
# for k in range(N + 1):
#     diff.append(road[k+1] - road[k])
# print(diff)
# diff = sorted(diff)
# for m in range(M):
#     print(diff)
#     maximum = diff.pop()
#     first = maximum // 2
#     second = maximum - first
#     diff.extend([first, second])
#     diff.sort()
#
# print(road)
# print(diff)

N, M, L = map(int, input().split())
road = [0]
road.extend(list(map(int, input().split())))
road.append(L)
road = sorted(road)

left = 0
right = L-1
result = 0
while left <= right:
    mid = (left+right) // 2
    count = 0 # 설치한 휴게소의 수
    for i in range(1, len(road)):
        if road[i] - road[i-1] > mid:
            count += (road[i] - road[i-1] -1)//mid

    if count > M:
        left = mid + 1
    else:
        result = mid
        right = mid - 1

print(result)

