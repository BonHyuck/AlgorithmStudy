N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: x[1])
for x, y in arr:
    print(x, y)
