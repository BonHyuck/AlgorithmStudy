# 4485. [G4] 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485

TC = 1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 계속 반복
while True:
    N = int(input())
    # N이 0이라면 더이상 입력이 들어오지 않기에 반복문을 멈춘다.
    if N == 0:
        break
    # 젤다가 가야하는 동굴
    box = [list(map(int, input().split())) for _ in range(N)]
    # 동굴의 각 지점에서 젤다가 잃는 최소값
    # 최소값으로 구해야하기때문에 초기값은 제일 큰 값으로 설정해둔다.
    dp = [[float('inf') for _ in range(N)] for _ in range(N)]
    # 시작점에선 다른 연산없이 해당 지점의 루피를 잃는다.
    dp[0][0] = box[0][0]
    # 시작
    queue = [(0, 0)]
    while queue:
        row, col = queue.pop(0)
        # 이동할 수 있는 4방향 확인
        for k in range(4):
            new_r = row + dr[k]
            new_c = col + dc[k]
            if 0 <= new_r < N and 0 <= new_c < N:
                # 현재 지점에서 다음 지점으로 이동할때
                # 1. 현재 지점까지 잃은 루피에서 다음 지점에서 잃을 루피의 합과
                # 2. 다음 지점에서 이미 잃은 루피값을 비교한다.
                # 1번값이 더 작다면 1번처럼 움직이는 것이 최적의 경로이다.
                if dp[row][col] + box[new_r][new_c] < dp[new_r][new_c]:
                    queue.append((new_r, new_c))
                    dp[new_r][new_c] = dp[row][col] + box[new_r][new_c]
    print("Problem {}: {}".format(TC, dp[N-1][N-1]))
    TC += 1