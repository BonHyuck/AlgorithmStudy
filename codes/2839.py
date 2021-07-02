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

N = int(input())
result = 0
while N >= 0:
    if N % 5 == 0:
        result += N // 5
        print(result)
        break
    N -= 3
    result += 1
else:
    print(-1)