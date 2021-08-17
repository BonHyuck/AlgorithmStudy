import sys
from collections import deque
text = sorted(list(sys.stdin.readline()))
N = len(text)
queue = deque()
for k in range(N // 2 + N % 2, N):
    queue.append(text[k])
result = text[0:N // 2 + N % 2]
idx = N // 2 - 1
queue = sorted(queue)
while idx >= 0:
    for k in range(len(queue)):
        if text[idx] != queue[k]:
            result.append(queue.pop(k))
            idx -= 1
            break

print(''.join(result))