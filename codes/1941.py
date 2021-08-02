# 1941. [G3] 소문난 칠공주
# https://www.acmicpc.net/problem/1941

from itertools import combinations

index_list = [i for i in range(25)]
text_list = []
for k in range(5):
    text_list.extend(list(input()))
comb = list(combinations(index_list, 7))
result = 0
for possible in comb:
    cnt = 0
    for k in possible:
        if text_list[k] == "S":
            cnt += 1
    if cnt >= 4:
        visited = [0 for _ in range(7)]
        visited[0] = 1
        queue = [0]
        while queue:
            point_index = queue.pop(0)
            point = possible[point_index]
            for i in range(7):
                if i != point_index and visited[i] == 0:
                    if point // 5 == possible[i] // 5 and abs(point % 5 - possible[i] % 5) == 1:
                        queue.append(i)
                        visited[i] = 1
                    elif point % 5 == possible[i] % 5 and abs(point // 5 - possible[i] // 5) == 1:
                        queue.append(i)
                        visited[i] = 1
        if visited.count(0) == 0:
            result += 1
print(result)
