# 1138. 한 줄로 서기
# https://www.acmicpc.net/problem/1138
N = int(input())
# 입력값
arr = list(map(int, input().split()))
# 줄 서는 자리
places = [0 for _ in range(N)]

# 1번 사람부터 확인한다.
for person in range(1, N+1):
    # 인덱스 맞추기 위해서 -1
    index = person - 1
    # 내 왼쪽에 있는 사람 수
    left_people = 0
    # 내 왼쪽에 있어야하는 사람 수
    need_people = arr[index]
    for now in range(N):
        # 왼쪽에 실제로 있는 사람과 왼쪽에 필요한 사람 수가 같으며
        # 현재 위치에 아무도 서있지 않음
        if left_people == need_people and places[now] == 0:
            places[now] = person
            break
        # 다른 키 큰 사람이 왼쪽에 올 것이니까 넘어간다.
        elif places[now] == 0:
            left_people += 1
        # 이미 누가 있음
        # 1부터 시작하는 반복문이므로 이미 누가 있더라도
        # 현재 사람보다 키가 작을 것이기 때문에
        # 그냥 넘어간다
        else:
            continue
print(*places)