'''
4
3 5 2 7

4
9 5 4 8
'''

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
result = [-1 for _ in range(N)]
stack = [0]

for k in range(1, N):
    while len(stack) > 0 and numbers[stack[-1]] < numbers[k]:
        result[stack.pop()] = numbers[k]
    stack.append(k)
print(*result)