# 2775. 부녀회장이 될테야(B2)
# https://www.acmicpc.net/problem/2775

# 테스트 케이스
T = int(input())
for test_case in range(T):
    # 층 = 행
    k = int(input())
    # 호 = 열
    n = int(input())
    # 아파트 형성
    box = [[0 for _ in range(n+1)] for _ in range(k+1)]
    # 0층에 값 넣기, 0층의 h호에는 h명이 산다.
    for h in range(1, n+1):
        box[0][h] = h
    # 1층부터 올라가면서 합계산
    for r in range(1, k+1):
        for c in range(1, n+1):
            box[r][c] = sum(box[r-1][1:c+1])
    print(box[k][n])
