# 2470. 두 용액
# https://www.acmicpc.net/problem/2470

N = int(input())
arr = list(map(int, input().split()))
# 배열 정렬
arr = sorted(arr)
# 시작점 = index
start = 0
# 끝 점 = index
end = N - 1
# 결과값, 0에 가까워져야함
result = float('inf')
# 결과값 = index
start_result = 0
# 결과값 = index
end_result = 0


while start < end:
    # 두 용액을 섞는다.
    mixed_value = arr[end] + arr[start]
    # 섞은 값의 절대값이 현재 결과값보다 작으면 (0에 더 가까움)
    if abs(mixed_value) < result:
        # 결과값 바꿔주기
        result = abs(mixed_value)
        start_result = start
        end_result = end
    # 현재 결과값이 + 라면 
    # 더 작게 만들어야한다.
    if mixed_value > 0:
        end -= 1
    # 현재 결과값이 - 라면
    # 더 크게 만들어야한다.
    elif mixed_value < 0:
        start += 1
    # 0이라면
    # 끝
    else:
        break

print(arr[start_result], arr[end_result])