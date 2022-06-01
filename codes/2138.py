import copy

N = int(input())
switch = list(map(int, list(input())))
temp = copy.deepcopy(switch)
result = list(map(int, list(input())))
if switch == result:
    print(0)
else:
    cnt = 0
    for k in range(N):
        if k == 0:
            if switch != result:
                cnt += 1
                switch[k] = 1 - switch[k]
                switch[k + 1] = 1 - switch[k + 1]
        elif 1 <= k < N - 1:
            if switch[k - 1] != result[k - 1]:
                cnt += 1
                switch[k - 1] = 1 - switch[k - 1]
                switch[k] = 1 - switch[k]
                switch[k + 1] = 1 - switch[k + 1]
        elif k == N - 1:
            if switch[k - 1] != result[k - 1]:
                cnt += 1
                switch[k - 1] = 1 - switch[k - 1]
                switch[k] = 1 - switch[k]
    if switch == result:
        print(cnt)
    else:
        cnt = 0
        for k in range(N):
            if 1 <= k < N - 1:
                if temp[k - 1] != result[k - 1]:
                    cnt += 1
                    temp[k - 1] = 1 - temp[k - 1]
                    temp[k] = 1 - temp[k]
                    temp[k + 1] = 1 - temp[k + 1]
            elif k == N - 1:
                if temp[k - 1] != result[k - 1]:
                    cnt += 1
                    temp[k - 1] = 1 - temp[k - 1]
                    temp[k] = 1 - temp[k]
        if temp == result:
            print(cnt)
        else:
            print(-1)