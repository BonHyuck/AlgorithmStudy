N, M = map(int, input().split())
arr = [0 for _ in range(N)]
result = 0
# 오름차순이니까 뒤에서부터 채우기
for k in range(N):
    arr[N-k-1] = int(input())

# 확인할 액수의 위치
idx = 0
# 돈이 남아있을동안 계속
while M > 0:
    # 현재 금액보다 동전의 액수가 큼
    if arr[idx] > M:
        idx += 1
        continue
    # 둘이 같으면 동전 1개만 늘어나고 끝
    elif arr[idx] == M:
        result += 1
        break
    # 현재 금액보다 동전의 액수가 작음
    else:
        # 동전 개수 구하기
        result += M // arr[idx]
        # 남은 금액 산출
        M = M % arr[idx]
        # 다음 돈 확인
        idx += 1

print(result)