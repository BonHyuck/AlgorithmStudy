# def start_select(index, weight, value):
#     global max_value
#
#     if weight > K:
#         return
#
#     if index >= N:
#         if max_value < value:
#             max_value = value
#         return
#     # 해당 인덱스의 물건 선택
#     start_select(index + 1, weight + box[index][0], value + box[index][1])
#     # 선택 안하고 넘어가기
#     start_select(index + 1, weight, value)
#
#     return
#
#
# N, K = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(N)]
# max_value = 0
# start_select(0, 0, 0)
# print(max_value)

N, K = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
box = sorted(box, key=lambda x: x[1])
