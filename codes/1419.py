'''
11
30
4
'''

# # 1419. [G4] 등차수열의 합
# # https://www.acmicpc.net/problem/1419
#
# left = int(input())
# right = int(input())
# k = int(input())
# result = 0
# # 숫자 = 2x + d
# # 3부터 전부 가능
# if k == 2:
#     # right가 3보다 작으면 없음
#     if right < 3:
#         result = 0
#     else:
#         if left < 3:
#             result = right - 3 + 1
#         else:
#             result = right - left + 1
# # 숫자 = 3x + 3d = 3(x + d)
# # 범위 안에서 6보다 크거나 같은 3의 배수
# elif k == 3:
#     if right < 6:
#         result = 0
#     else:
#         if left < 6:
#             result = right // 3 - 1
#         else:
#             result = right // 3 - left // 3
#         if left % 3 == 0:
#             result += 1
# # 숫자 = 4x + 6d = 4(x + d) + 2d
# # 범위 안에서 10보다 크거나 같으면서 4로 나눴을때 나머지가 0 혹은 2 = 2의 배수
# # 근데 12는 안됨ㅋ
# # 10, 14, 16, 18, 20, ...
# elif k == 4:
#     if right < 10:
#         result = 0
#     elif right < 14:
#         if left <= 10:
#             result = 1
#         else:
#             result = 0
#     else:
#         if left <= 10:
#             result = right // 2 - 5
#         elif left <= 14:
#             result = right // 2 - 6
#         else:
#             # left > 14
#             result = right // 2 - left // 2
#             if left % 2 == 0:
#                 result += 1
# # 숫자 = 5x + 10d = 5(x + 2d)
# # 15부터 시작하는 5의 배수
# elif k == 5:
#     if right < 15:
#         result = 0
#     else:
#         if left < 15:
#             result = right // 5 - 2
#         else:
#             result = right // 5 - left // 5
#         if left % 5 == 0:
#             result += 1
#
# print(result)

# 1419. [G4] 등차수열의 합
# https://www.acmicpc.net/problem/1419

left = int(input())
right = int(input())
k = int(input())
result = 0
if k == 2:
    # right가 3보다 작으면 없음
    if right < 3:
        result = 0
    else:
        # left가 1 혹은 2라면
        if left < 3:
            # 기준값 3을 가지고 범위 설정
            result = right - 3 + 1
        else:
            # left와 right 사이의 모든 수
            result = right - left + 1
# 홀수일 경우 (3, 5)
elif k == 3 or k == 5:
    # 기준 숫자
    start_number = (k * (k + 1)) // 2
    # 기준 숫자가 left보다 작으면
    if start_number < left:
        # 일정 규칙을 가지고 순환하기 때문에
        # 해당 규칙내에서 left 이상이면서 제일 가까운 숫자를 기준 숫자로 설정
        start_number += ((((left - start_number) // k) + 1) * k)
        # 만일 left가 규칙 내에 있으면
        # 기준 숫자에서 k를 빼줘서 left로 만들어 준다.
        # start_number = left
        if left % k == 0:
            start_number -= k
    # 기준 숫자가 right 이하일 경우
    # right 초과라면 결과는 0
    if start_number <= right:
        result = ((right - start_number) // k) + 1
elif k == 4:
    # left가 1 ~ 10 사이
    if 1 <= left <= 10:
        # right가 10보다 작으면 결과 없음
        # k = 4를 만족하는 최소 숫자는 10이기 때문
        if right < 10:
            result = 0
        else:
            # 기준 값을 14로 잡는다
            # 10부터 시작해서 2씩 커지나
            # 12는 제외되기 때문에
            start_number = 14
            # 만일 기준숫자 = 14가 left보다 작으면
            if start_number < left:
                # left가 짝수라면 규칙에 들어오는 숫자
                if left % 2 == 0:
                    start_number = left
                # left가 홀수라면 그 다음 수가 규칙에 들어오는 숫자
                else:
                    start_number = left + 1
            # 기준숫자가 right보다 작으면 계산
            # 기준숫자가 right보다 크면 결과값은 0
            if start_number <= right:
                result = (right - start_number) // 2 + 1
            # 10을 포함시켜주기
            result += 1
    else:
        # left가 10 초과면
        # 10을 포함하지 않으므로 기준 값을 14부터 바로 시작
        start_number = 14
        if start_number < left:
            if left % 2 == 0:
                start_number = left
            else:
                start_number = left + 1
        if start_number <= right:
            result = (right - start_number) // 2 + 1
print(result)


