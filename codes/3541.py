'''
10 3
15 12
15 4
7 12
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = float('inf')

for k in range(M):
    U, D = map(int, input().split())
    for n in range(N, -1, -1):
        temp = U * n - D * (N - n)
        if temp > 0:
            result = min(result, temp)
        else:
            break

print(result)


