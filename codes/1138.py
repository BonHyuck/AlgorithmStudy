N = int(input())
arr = list(map(int, input().split()))
places = [0 for _ in range(N)]

for person in range(1, N+1):
    index = person - 1
    left_people = 0
    need_people = arr[index]
    for now in range(N):
        # 왼쪽에 실제로 있는 사람과 왼쪽에 필요한 사람 수가 같으며
        # 현재 위치에 아무도 서있지 않음
        if left_people == need_people and places[now] == 0:
            places[now] = person
            break
        # 다른 사람이 왼쪽에 올 것이니까 넘어간다.
        elif places[now] == 0:
            left_people += 1
        # 이미 누가 있음 (현재 사람보다 작은 사람)
        else:
            continue
print(*places)