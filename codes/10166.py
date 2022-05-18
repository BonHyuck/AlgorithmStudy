import math
D1, D2 = map(int, input().split())
result = 0
arr = [{} for _ in range(D2 + 1)]

for k in range(D1, D2 + 1):
    for i in range(1, k + 1):
        number = math.gcd(k, i)
        if arr[i // number].get(k // number, 0) == 0:
            arr[i // number][k // number] = 1
            result += 1

print(result)
