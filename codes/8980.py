N, C = map(int, input().split())
M = int(input())
box = [list(map(int, input().split())) for _ in range(M)]

# 배송 순서가 빠른 것부터 앞으로
box = sorted(box, key=lambda x: x[1])

result = 0
remain = [C] * (N + 1)  # 각 위치에 남은 공간

for i in range(M):
    temp = C  # c개를 옮길 수 있다고 가정
    for j in range(box[i][0], box[i][1]):
        temp = min(temp, remain[j])
    temp = min(temp, box[i][2])
    for j in range(box[i][0], box[i][1]):
        remain[j] -= temp
    result += temp

print(result)