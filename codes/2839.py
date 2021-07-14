# def find_bag(three, five):
#     global result
#
#     if 3 * three + 5 * five == N:
#         if result > three + five:
#             result = three + five
#         return
#
#     if 3 * three + 5 * five > N:
#         return
#
#     find_bag(three, five + 1)
#     find_bag(three + 1, five)
#
#     return
#
# N = int(input())
# result = float('inf')
# find_bag(0, 0)
# if result == float('inf'):
#     result = -1
# print(result)

# 2839. 설탕 배달(B1)
# https://www.acmicpc.net/problem/2839

N = int(input())
result = 0
while N >= 0:
    # 무거운 포대를 우선적으로 사용해야
    # 최소 개수가 된다.
    # 무거운 포대 3개 = 가벼운 포대 5개
    # 간단한 수학
    if N % 5 == 0:
        result += N // 5
        print(result)
        break
    N -= 3
    result += 1
else:
    print(-1)