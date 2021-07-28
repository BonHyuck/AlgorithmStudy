# def SOD(number):
#     result = 0
#
#     for k in range(2, int(number ** (1/2)) + 1):
#         if number % k == 0:
#             if number // k == k:
#                 result += k
#             else:
#                 result += k + number // k
#     return result
#
#
# N = int(input())
# result = 0
# for k in range(1, N + 1):
#     result += SOD(k)
# print(result)

# def CSOD(number):
#     result = 0
#
#     for selected_number in range(4, number + 1):
#         divisor = 2
#         while divisor ** 2 <= selected_number:
#             if selected_number % divisor == 0:
#                 if selected_number // divisor == divisor:
#                     result += divisor
#                 else:
#                     result += divisor + selected_number // divisor
#             divisor += 1
#     return result
#
# N = int(input())
# print(CSOD(N) % 1000000)

def CSOD(number):
    result = 0
    i = 2
    while i * i <= number:
        j = number // i
        result += (i + j) * (j - i + 1) // 2
        result += i * (j - i)
        i += 1
    return result

N = int(input())
print(CSOD(N) % 1000000)


