# 1941. [G3] 소문난 칠공주
# https://www.acmicpc.net/problem/1941

# 5 x 5의 배열에서 25C7이었기에 시간복잡도가 아주 크진 않을것이라 판단

from itertools import combinations

# 5 x 5 이므로 좌상단부터 우하단까지
# 0부터 채우면 24까지 채워진다.
index_list = [i for i in range(25)]
# 파벌을 넣는다.
text_list = []
for k in range(5):
    text_list.extend(list(input()))
# 7명이 1 그룹이므로 경우의 수를 모두 구해둔다.
comb = list(combinations(index_list, 7))
result = 0
# 조합을 모두 검사
for possible in comb:
    # 다솜파가 4명 이상 있어야한다.
    cnt = 0
    for k in possible:
        if text_list[k] == "S":
            cnt += 1
    if cnt >= 4:
        # 7명이 인접한지 확인한다.
        visited = [0 for _ in range(7)]
        visited[0] = 1
        # 0번째 부터 확인
        queue = [0]
        while queue:
            point_index = queue.pop(0)
            # point = 해당 사람의 번호
            point = possible[point_index]
            for i in range(7):
                # 아직 방문이 안됐다면
                if i != point_index and visited[i] == 0:
                    # 같은 col에 있으면서 row의 차이가 1 = 인접
                    if point // 5 == possible[i] // 5 and abs(point % 5 - possible[i] % 5) == 1:
                        queue.append(i)
                        visited[i] = 1
                    # 같은 row에 있으면서 col의 차이가 1 = 인접
                    elif point % 5 == possible[i] % 5 and abs(point // 5 - possible[i] // 5) == 1:
                        queue.append(i)
                        visited[i] = 1
        # 인접 확인을 끝내고 모두 방문이 가능했다면
        # 결과값에 1 추가
        if visited.count(0) == 0:
            result += 1
print(result)
