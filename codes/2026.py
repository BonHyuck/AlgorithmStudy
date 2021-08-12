"""
4 6 8
1 2
1 3
1 6
2 3
2 6
3 6
4 5
5 6
"""


def find_friend(text, idx):
    global result

    temp_arr = text.split()

    visited[idx] = 1
    temp_arr.append(str(idx))

    if K == len(temp_arr):
        if len(result.split()) != K:
            result = " ".join(temp_arr)
        return

    for next_index in range(idx + 1, N + 1):
        if visited[next_index] == 0:
            all_friend = True
            for friend in temp_arr:
                if arr[int(friend)][next_index] == 0:
                    all_friend = False
                    break
            if all_friend:
                find_friend(' '.join(temp_arr), next_index)

K, N, F = map(int,input().split())
arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for k in range(F):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1
result = ""
# 모든 점에서 시작해보자
for k in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    find_friend("", k)
    if len(result.split()) == K:
        break
if len(result.split()) == K:
    for k in result.split():
        print(k)
else:
    print(-1)