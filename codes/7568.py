N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
cnt = [1 for _ in range(N)]

for i in range(N):
    for j in range(i, N):
        one_W, one_H = people[i]
        two_W, two_H = people[j]
        if one_W > two_W and one_H > two_H:
            cnt[j] += 1
        elif one_W < two_W and one_H < two_H:
            cnt[i] += 1

print(*cnt)