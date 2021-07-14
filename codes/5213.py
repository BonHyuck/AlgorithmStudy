import sys
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def find_path(row, col, dominoes):
    global result, domino_length
    if box[row][col][0] == last_number:
        if len(dominoes) < domino_length:
            result = dominoes
            domino_length = len(dominoes)

    if len(dominoes) >= domino_length:
        return

    for k in range(4):
        new_r = row + dx[k]
        new_c = col + dy[k]
        # 인덱스 확인
        if 0 <= new_r < N and 0 <= new_c < N * 2:
            # 아직 방문 안 한 곳으로 가기
            if visited[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                # 다른 도미노
                if box[row][col][0] != box[new_r][new_c][0]:
                    # 다른 도미노이지만 인접
                    if box[row][col][0] != box[new_r][new_c][0] and box[row][col][1] == box[new_r][new_c][1]:
                        find_path(new_r, new_c, dominoes + " " + str(box[new_r][new_c][0]))
                    # 인접도 안하고 다른 도미노이지만 마지막 도미노와 연결돼있음
                    elif box[new_r][new_c][0] == last_number:
                        find_path(new_r, new_c, dominoes)
                # 같은 도미노
                else:
                    find_path(new_r, new_c, dominoes)

                visited[new_r][new_c] = 0


N = int(sys.stdin.readline())
box = [[(-1, -1) for _ in range(N * 2)] for _ in range(N)]
domino_list = [(-1, -1) for _ in range(N*N - N//2 + 1)]
number = 1
for r in range(N):
    if r % 2 == 0:
        for c in range(0, N * 2, 2):
            one, two = map(int, sys.stdin.readline().split())
            box[r][c] = (number, one)
            box[r][c + 1] = (number, two)
            domino_list[number] = (one, two)
            number += 1
    else:
        for c in range(1, N * 2 - 2, 2):
            one, two = map(int, sys.stdin.readline().split())
            box[r][c] = (number, one)
            box[r][c + 1] = (number, two)
            domino_list[number] = (one, two)
            number += 1
last_number = box[N - 1][N * 2 - 1][0]
if last_number == -1:
    last_number = box[N - 1][N * 2 - 2][0]
print(last_number)
queue = [(0, 0)]
domino_length = float('inf')
result = ''
visited = [[0 for _ in range(N * 2)] for _ in range(N)]
visited[0][0] = 1
find_path(0, 0, '1')
print(result.count(" ") + 1)
print(result)
