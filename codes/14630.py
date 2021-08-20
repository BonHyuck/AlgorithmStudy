'''
3
11
33
55
1 3
'''

def find_path(idx, dist):
    global result
    if dist > result:
        return

    if idx == end:
        if dist < result:
            result = dist
        return




N = int(input())
parts = list(input() for _ in range(N))
money = [[float('inf') for _ in range(N)] for _ in range(N)]
for start in range(N):
    for end in range(N):
        total = 0
        if start != end:
            for k in range(len(parts[start])):
                total += int((int(parts[start][k]) - int(parts[end][k])) ** 2)
            money[start][end] = total
            money[end][start] = total

start, end = map(int, input().split())
start -= 1
end -= 1
result = float('inf')

visited = [[0 for _ in range(N)] for _ in range(N)]

find_path(start, 0)

print(money)
print(parts)
