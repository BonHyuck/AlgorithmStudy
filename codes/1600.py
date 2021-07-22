
monkey_r = [-1, 1, 0, 0]
monkey_c = [0, 0, -1, 1]
horse_r = [-1, -2, -2, -1, 1, 2, 2, 1]
horse_c = [-2, -1, 1, 2, 2, 1, -1, -2]

def find_path(row, col, cnt):
    visited[row][col] = 1

    if cnt > 0:
        for k in range(8):
            new_r = 

K = int(input())
N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
result = float('inf')
find_path(0, 0, K)