# def find_sequence(text, idx, length):
#     global result_text, result_length
#     if idx == N:
#         if length > result_length:
#             result_length = length
#         return
#
#     temp_arr = text.split()
#     if len(temp_arr) > 0:
#         compare_number = int(temp_arr[-1])
#         if compare_number < arr[idx]:
#             find_sequence(text + " " + str(arr[idx]), idx + 1, length + 1)
#         find_sequence(text, idx + 1, length)
#     else:
#         find_sequence(text + " " + str(arr[idx]), idx + 1, length + 1)
#
#     return
#
#
# N = int(input())
# arr = list(map(int, input().split()))
# result_length = 0
# find_sequence("", 0, 0)
# print(result_length)

N = int(input())
arr = list(map(int, input().split()))
cnt_arr = []
for i in range(N):
    number = arr[i]
    next_cnt = 1
    for j in range(i):
        compare = arr[j]
        if number > compare:
            next_cnt = max(next_cnt, cnt_arr[j] + 1)
    cnt_arr.append(next_cnt)
print(max(cnt_arr))


