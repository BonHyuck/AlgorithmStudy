T = int(input())

for t in range(T):
    A, B, C = map(int, input().split())
    AB, BC, CA = map(int, input().split())

    result = 0
    for i in range(min(A, B) + 1):
        for j in range(min(B - i, C) + 1):
            k = min(A - i, C - j)
            result = max(result, AB * i + BC * j + CA * k)

    print(result)
