# # 1563. [G4] 개근상
# # https://www.acmicpc.net/problem/1563
# import sys
# sys.setrecursionlimit(100000)
#
#
# def find_student(day, late, absent):
#     if late >= 2 or absent >= 3:
#         return 0
#
#     if day == N:
#         return 1
#
#     result = dp[day][late][absent]
#     if result != -1:
#         return result
#
#     result = find_student(day + 1, late, 0) + find_student(day+1, late + 1, 0) + find_student(day + 1, late, absent + 1)
#
#     return result % 1000000
#
# N = int(input())
#
# # [일][지각횟수][결석횟수]
# dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(N+1)]
#
# print(find_student(0, 0, 0))


# 1563. [G4] 개근상
# https://www.acmicpc.net/problem/1563
import sys
sys.setrecursionlimit(1000000)


def find_student(day, late, absent):
    if late >= 2 or absent >= 3:
        return 0

    if day == N:
        return 1

    if dp[day][late][absent] == -1:
        result = find_student(day + 1, late, 0) + find_student(day+1, late + 1, 0) + find_student(day + 1, late, absent + 1)
        dp[day][late][absent] = result
        return result
    else:
        return dp[day][late][absent]

N = int(input())

# [일][지각횟수][결석횟수]
dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(N+1)]

print(find_student(0, 0, 0) % 1000000)