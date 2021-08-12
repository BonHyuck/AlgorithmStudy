# 2023. [G5] 신기한 소수
# https://www.acmicpc.net/problem/2023

N = int(input())
# 다음으로 붙을 수 있는 수
# 0, 짝수, 5 안됨
possible = [1, 3, 7, 9]
result = []
# 1자리 수 소수들
prev_queue = [2, 3, 5, 7]
if N == 1:
    result = [2, 3, 5, 7]
else:
    while prev_queue:
        # 소수 1개 가져오기
        prev_number = prev_queue.pop(0)
        # 길이가 N이면 결과값에 넣기
        if len(str(prev_number)) == N:
            result.append(prev_number)
            continue
        # 뒤에 붙는 모든 경우 검사
        # = 1, 3, 7, 9
        for k in possible:
            number = int(str(prev_number) + str(k))
            # 약수 검사
            for divisor in range(2, int(number ** (1/2))):
                if number % divisor == 0:
                    break
            # break가 아닌 전체 범위 검사 이후 반복문이 종료되면
            else:
                # 큐에 붙여서 다음에 검사
                prev_queue.append(number)

for r in result:
    print(r)
