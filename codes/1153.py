# 1153. [G4] 네 개의 소수
# https://www.acmicpc.net/problem/1153

N = int(input())
arr = [0 for _ in range(N+1)]
# 소수만 남기기
# arr[i] = 0 => i = 소수
for k in range(2, N+1):
    if arr[k] == 0:
        for i in range(k, N+1, k):
            if k != i:
                arr[i] = 1

result = []
# 8보다 작으면 2+2+2+2 보다 작기 때문에 불가능함
if N < 8:
    print(-1)
# 골드바흐의 추측
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