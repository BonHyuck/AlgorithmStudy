N = int(input())
arr = [0 for _ in range(N+1)]
for k in range(2, N+1):
    if arr[k] == 0:
        for i in range(k, N+1, k):
            if k != i:
                arr[i] = 1

# primes = []
# for i in range(2, N+1):
#     if arr[i] == 0:
#         primes.append(i)

result = []
if N < 8:
    print(-1)
else:
    if N % 2 == 0:
        result.extend([2, 2])
        N -= 4
    else:
        result.extend([2, 3])
        N -= 5
    for i in range(2, N + 1):
        if arr[i] == 0 and arr[N - i] == 0:
            result.extend([i, N - i])
            break
    print(*result)