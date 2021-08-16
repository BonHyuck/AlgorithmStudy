# 집합의 크기
L = int(input())
# 집합
arr = list(map(int, input().split()))
arr.append(0)
arr = sorted(arr)
# 구해야할 수의 개수
N = int(input())

for k in range(1, L + 1):
    if arr[k] - arr[k-1] == 1:
        continue
    if arr[k] - arr[k - 1] <= 220:
        for i in range(arr[k-1] + 1, arr[k]):

