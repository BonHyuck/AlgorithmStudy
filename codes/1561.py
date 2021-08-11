# 1561. [G2] 놀이 공원
# https://www.acmicpc.net/problem/1561

N, M = map(int, input().split())
arr = list(map(int, input().split()))
time = 0
people = 0
left = 0
right = 2000000001
while left <= right:
    mid = (left + right) // 2
    temp_people = 0
    for minute in arr:
        temp_people += ((mid - 1) // minute) + 1
    if temp_people >= N:
        right = mid - 1
    else:
        if time < mid:
            time = mid
            people = temp_people
        left = mid + 1

if N <= M:
    print(N)
else:
    for k in range(M):
        minute = arr[k]
        if time % minute == 0:
            people += 1
            if people == N:
                print(k + 1)
                break
# N, M = map(int, input().split())
# temp = list(map(int, input().split()))
# arr = []
# for k in range(M):
#     arr.append((k + 1, temp[k]))
# if N <= M:
#     print(N)
# else:
#     arr = sorted(arr, key=lambda x:x[1])
#     print(arr[(N + 1) % M][0])