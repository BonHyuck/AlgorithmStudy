# def solution(n, left, right):
#     arr = [[0 for _ in range(n)] for _ in range(n)]
#
#     for i in range(n):
#         for r in range(i + 1):
#             arr[r][i] = i + 1
#         for c in range(i + 1):
#             arr[i][c] = i + 1
#         # for r in range(i + 1):
#         #     for c in range(i + 1):
#         #         if arr[r][c] == 0:
#         #             arr[r][c] = i + 1
#     # print(arr)
#     new_arr = []
#     for k in arr:
#         new_arr.extend(k)
#
#     return new_arr[left:right + 1]

def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))