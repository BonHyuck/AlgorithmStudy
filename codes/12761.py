A, B, N, M = map(int, input().split())
result = 0
# 이동 가능한 경우의 수
jumps = [1, -1, A, -A, B, -B, A, B]
# 징검다리(방문 처리)
stones = [0 for _ in range(100001)]
# 현재 위치 표시
stones[N] = 1
# 시작점
queue = [[N]]
while queue:
    result += 1
    # 다음 단계 배열
    new_arr = []
    possible = queue.pop(0)
    found = False
    while possible:
        step = possible.pop(0)
        # 하나의 자리에서 8개의 경우의 수가 있다
        for k in range(8):
            next_step = step + jumps[k]
            # 곱연산
            if k > 5:
                next_step = step * jumps[k]
            if 0 <= next_step <= 100000 and next_step != M and stones[next_step] == 0:
                stones[next_step] = 1
                new_arr.append(next_step)
            elif next_step == M:
                found = True
                break
    # 아직 만나지 못함
    if not found:
        queue.append(new_arr)
    else:
        break

print(result)

