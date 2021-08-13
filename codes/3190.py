dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
box = [[0 for _ in range(N)] for _ in range(N)]
K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    box[row - 1][col - 1] = 1
L = int(input())
times = [0 for _ in range(10001)]
for k in range(L):
    time, dir = input().split()
    times[int(time)] = dir

dir = 1
time = 1
queue = [(0, 0)]
row = col = 0
box[row][col] = 2

while True:
    row += dr[dir]
    col += dc[dir]
    if 0 <= row < N and 0 <= col < N and box[row][col] != 2:
        if box[row][col] != 1:
            new_r, new_c = queue.pop(0)
            box[new_r][new_c] = 0
        box[row][col] = 2
        queue.append((row, col))
        if times[time] == "L":
            dir = (dir - 1) % 4
        elif times[time] == "D":
            dir = (dir + 1) % 4
        time += 1
    else:
        break
print(time)
