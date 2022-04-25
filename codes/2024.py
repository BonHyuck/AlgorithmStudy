import sys
input = sys.stdin.readline

M = int(input())
lines = []
while True:
    l, r = map(int, input().split())
    if l == 0 and r == 0:
        break
    if r < 0 or l > M or l == r:
        continue

    lines.append((l, r))
lines = sorted(lines, key=lambda x: (x[0], x[1]))

start = 0
idx = 0
result = 0

while True:
    temp = -1

    while idx < len(lines):
        left = lines[idx][0]
        right = lines[idx][1]
        if left <= start:
            if right > temp:
                temp = right
        else:
            break
        idx += 1

    if temp == -1:
        result = 0
        break

    result += 1
    if temp >= M:
        break

    start = temp

print(result)