# 2023. [G5] 신기한 소수
# https://www.acmicpc.net/problem/2023

N = int(input())
possible = [1, 3, 7, 9]
result = []
prev_queue = [2, 3, 5, 7]
if N == 1:
    result = [2, 3, 5, 7]
else:
    while prev_queue:
        prev_number = prev_queue.pop(0)
        if len(str(prev_number)) == N:
            result.append(prev_number)
            continue
        for k in possible:
            number = int(str(prev_number) + str(k))
            for divisor in range(2, int(number ** (1/2))):
                if number % divisor == 0:
                    break
            else:
                prev_queue.append(number)

for r in result:
    print(r)
