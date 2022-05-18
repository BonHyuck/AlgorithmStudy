T = int(input())
arr = [[0 for _ in range(10)] for _ in range(1001)]
for i in range(10):
    arr[1][i] = 1

for i in range(2, 1001):
    for j in range(10):
        if j == 0:
            arr[i][j] = arr[i - 1][7]
        elif j == 1:
            arr[i][j] = arr[i - 1][2] + arr[i - 1][4]
        elif j == 2:
            arr[i][j] = arr[i - 1][1] + arr[i - 1][3] + arr[i - 1][5]
        elif j == 3:
            arr[i][j] = arr[i - 1][2] + arr[i - 1][6]
        elif j == 4:
            arr[i][j] = arr[i - 1][1] + arr[i - 1][5] + arr[i - 1][7]
        elif j == 5:
            arr[i][j] = arr[i - 1][2] + arr[i - 1][4] + arr[i - 1][6] + arr[i - 1][8]
        elif j == 6:
            arr[i][j] = arr[i - 1][3] + arr[i - 1][5] + arr[i - 1][9]
        elif j == 7:
            arr[i][j] = arr[i - 1][0] + arr[i - 1][4] + arr[i - 1][8]
        elif j == 8:
            arr[i][j] = arr[i - 1][5] + arr[i - 1][7] + arr[i - 1][9]
        elif j == 9:
            arr[i][j] = arr[i - 1][6] + arr[i - 1][8]

for t in range(T):
    N = int(input())
    result = 0
    for k in range(10):
        result += arr[N][k]
    print(result % 1234567)