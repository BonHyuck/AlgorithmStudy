D1, D2 = map(int, input().split())
arr = [0 for _ in range(720001)]

for i in range(D1, D2 + 1):
    number = 360 * 2000 // i
    temp = number
    if arr[0] == 0:
        arr[0] = 1
    while number < 360 * 2000:
        if arr[number] == 0:
            arr[number] = 1
        number += temp

print(arr.count(1))