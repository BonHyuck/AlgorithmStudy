'''
5 3
1 2
6 3
4 1
3 2
0 2


7 7
1 2
2 4
2 2
4 4
5 3
7 5
5 7

13 5
1 1
2 1
3 1
4 1
5 1
6 1
7 1
3 3
4 4
6 3
7 5
8 3
9 5


'''
import sys
from collections import deque
input = sys.stdin.readline

N, T = map(int, input().split())

arr = [[] for _ in range(T + 1)]

max_x = 0
max_y = 0

for k in range(N):
    x, y = map(int, input().split())
    if y <= T:
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        arr[y].append(x)


queue = deque()
queue.append((0, 0, 0))
visited = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
result = -1

while queue:
    x, y, c = queue.popleft()
    if y == T:
        result = c
        break

    if 0 <= y - 2 <= T:
        for next_x in arr[y - 2]:
            if visited[y - 2][next_x] == 0:
                if abs(x - next_x) <= 2:
                    visited[y - 2][next_x] = 1
                    queue.append((next_x, y - 2, c + 1))
    if 0 <= y - 1 <= T:
        for next_x in arr[y - 1]:
            if visited[y - 1][next_x] == 0:
                if abs(x - next_x) <= 2:
                    visited[y - 1][next_x] = 1
                    queue.append((next_x, y - 1, c + 1))
    for next_x in arr[y]:
        if visited[y][next_x] == 0:
            if abs(x - next_x) <= 2:
                visited[y][next_x] = 1
                queue.append((next_x, y, c + 1))
    if y + 1 <= T:
        for next_x in arr[y + 1]:
            if visited[y + 1][next_x] == 0:
                if abs(x - next_x) <= 2:
                    visited[y + 1][next_x] = 1
                    queue.append((next_x, y + 1, c + 1))
    if y + 2 <= T:
        for next_x in arr[y + 2]:
            if visited[y + 2][next_x] == 0:
                if abs(x - next_x) <= 2:
                    visited[y + 2][next_x] = 1
                    queue.append((next_x, y + 2, c + 1))

print(result)

