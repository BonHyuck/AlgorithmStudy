'''
10
1 2 3 4 5 6 10 8 9 7

11
0 1 2 3 4 5 6 7 8 9 10
'''

import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))
result = 0

for idx, total in enumerate(numbers):
    start = 0
    end = len(numbers) - 1
    while start < end:
        if idx == end:
            end -= 1
            continue
        if idx == start:
            start += 1
            continue
        if total == numbers[start] + numbers[end]:
            result += 1
            break
        if total > numbers[start] + numbers[end]:
            start += 1
        else:
            end -= 1

print(result)