T = int(input())
for test_case in range(T):
    k = int(input())
    n = int(input())
    box = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for h in range(1, n+1):
        box[0][h] = h
    for r in range(1, k+1):
        for c in range(1, n+1):
            box[r][c] = sum(box[r-1][1:c+1])
    print(box[k][n])
