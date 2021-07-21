# 1245. [S1] 농장관리
# https://www.acmicpc.net/problem/1245

import sys

# x, y의 차가 1이하 = -1, 0, 1
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

# 함수
def find_mountain(row, col):
    global top
    # 8방향 전부 확인
    for k in range(8):
        # 옆에 있는 것
        new_r = row + dx[k]
        new_c = col + dy[k]
        # 인덱스 확인
        if 0 <= new_r < N and 0 <= new_c < M:
            # 현재보다 옆의 높이가 더 크다면 산봉우리 아님
            if box[row][col] < box[new_r][new_c]:
                top = False
            # 옆이 아직 방문을 안했고 현재 위치와 높이가 같다면
            if visited[new_r][new_c] == 0 and box[row][col] == box[new_r][new_c]:
                # 방문처리
                visited[new_r][new_c] = 1
                # 옆 농장의 주변 확인 시작
                find_mountain(new_r, new_c)
            else:
                continue
        else:
            continue
    return


N, M = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 방문 처리용 배열
visited = [[0 for _ in range(M)] for _ in range(N)]
# 결과 값
result = 0

# 배열 전부 확인
for r in range(N):
    for c in range(M):
        # 산이 있으며 아직 방문하지 않은 곳
        if box[r][c] != 0 and visited[r][c] == 0:
            # 일단 여기를 산봉우리라고 친다
            top = True
            # 함수 시작
            find_mountain(r, c)
            # 함수가 끝나고도 아직 산봉우리면 결과값에 1 추가
            if top:
                result += 1

print(result)