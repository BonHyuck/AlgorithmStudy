def find_sum(number):
    cnt_arr = [0 for _ in range(10)]
    left = 1
    right = number
    exp = 0

    while left <= right:
        while right % 10 != 9 and left <= right:
            temp = right
            while temp > 0:
                cnt_arr[temp % 10] += (10 ** exp)
                temp //= 10
            right -= 1
        if right < left:
            break
        while left % 10 != 0 and left <= right:
            temp = left
            while temp > 0:
                cnt_arr[temp % 10] += (10 ** exp)
                temp //= 10
            left += 1

        left //= 10
        right //= 10

        for k in range(10):
            cnt_arr[k] += (right - left + 1) * (10 ** exp)

        exp += 1

    result = 0
    for k in range(10):
        result += cnt_arr[k] * k

    return result

L, U = map(int, input().split())
print(find_sum(U) - find_sum(L - 1))