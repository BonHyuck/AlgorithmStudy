'''
5 2 10 0 0
1 0
2 0
4 0
6 0
8 0
'''

N, R, D, X, Y = map(int, input().split())
towers = [tuple(map(int, input().split())) for _ in range(N)]
# 적을 공격 가능한 모든 탑
attack = []
for r, c in towers:
    # 적과 탑의 거리 계산
    distance = ((abs(r - X) ** 2) + (abs(c - Y) ** 2)) ** 1/2
    # distance = abs(r - X) + abs(c - Y)
    if distance <= R:
        attack.append((r, c))

result = 0
while attack:
    attack_tower_R, attack_tower_C = attack.pop(0)
    queue = [[(attack_tower_R, attack_tower_C)]]
    visited = [0 for _ in range(N)]
    while True:
        tower_list = queue[-1]
        temp_list = []
        for start_tower_R, start_tower_C in tower_list:
            for k in range(N):
                next_tower_R, next_tower_C = towers[k]
                if next_tower_C == start_tower_C and next_tower_R == start_tower_R:
                    visited[k] = 1
                    continue
                if visited[k] == 0:
                    distance = ((abs(next_tower_C - start_tower_C) ** 2) + (abs(next_tower_R - start_tower_R) ** 2)) ** 1/2
                    # distance = abs(next_tower_C - start_tower_C) + abs(next_tower_R - start_tower_R)
                    if distance <= R:
                        visited[k] = 1
                        temp_list.append((next_tower_R, next_tower_C))
        if len(temp_list) > 0:
            queue.append(temp_list)
        else:
            break
    power = 0
    for idx in range(len(queue)-1, 0, -1):
        power = ((len(queue[idx]) * D) + power) / 2
    power += D

    print(queue)
    print(power)

    if result < power:
        result = power

print(round(result, 2))
