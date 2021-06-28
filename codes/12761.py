A, B, N, M = map(int, input().split())
result = 0
jumps = [1, -1, A, -A, B, -B, A, B]
stones = [0 for _ in range(100001)]
stones[N] = 1
queue = [[N]]
while queue:
    result += 1
    new_arr = []
    possible = queue.pop(0)
    found = False
    while possible:
        step = possible.pop(0)
        for k in range(8):
            next_step = step + jumps[k]
            if k > 5:
                next_step = step * jumps[k]
            if 0 <= next_step <= 100000 and next_step != M and stones[next_step] == 0:
                stones[next_step] = 1
                new_arr.append(next_step)
            elif next_step == M:
                found = True
                break
    if not found:
        queue.append(new_arr)
    else:
        break

print(result)

