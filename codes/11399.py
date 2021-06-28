N = int(input())
arr = list(map(int, input().split()))
arr.sort()

for k in range(1, N):
    arr[k] = arr[k-1] + arr[k]

print(sum(arr))

