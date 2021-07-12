# import sys
#
# shapes = {
#     1: [[(0, 0), (-1, 0), (-2, 0), (-3, 0)]],
#     2: [[(0, 0), (-1, 0), (-2, 0), (-2, 1)],
#         [(0, 0), (0, 1), (0, 2), (-1, 0)],
#         [(0, 0), (0, 1), (-1, 1), (-2, 1)],
#         [(0, 0), (-1, 0), (-1, -1), (-1, -2)]],
#     3: [[(0, 0), (-1, 0), (-2, 0), (-2, -1)],
#         [(0, 0), (0, 1), (0, 2), (-1, 2)],
#         [(0, 0), (0, 1), (-1, 0), (-2, 0)],
#         [(0, 0), (-1, 0), (-1, 1), (-1, 2)]],
#     4: [[(0, 0), (0, 1), (0, 2), (-1, 1)],
#         [(0, 0), (-1, 0), (-1, 1), (-2, 0)],
#         [(0, 0), (-1, 0), (-1, -1), (-1, 1)],
#         [(0, 0), (-1, 0), (-1, -1), (-2, 0)]],
#     5: [[(0, 0), (0, 1), (-1, 1), (-1, 2)],
#         [(0, 0), (-1, 0), (-1, -1), (-2, -1)]],
#     6: [[(0, 0), (-1, 0), (-1, -1), (0, 1)],
#         [(0, 0), (-1, 0), (-1, 1), (-2, 1)]],
#     7: [[(0, 0), (-1, 0), (-1, 1), (0, 1)]]
# }
#
# board = [[0 for _ in range(3)] for _ in range(300)]
# N = int(sys.stdin.readline())
# blocks = [int(sys.stdin.readline()) for _ in range(N)]

# import sys
#
# def find_height(index):
#     global result
#
#     if result < max(board):
#         return
#     if index >= N:
#         if result > max(board):
#             result = max(board)
#         return
#
#     # 각 블록별로 작업
#     if blocks[index] == 1:
#         # 0번째 칸에 들어감
#         board[0] += 4
#         find_height(index + 1)
#         board[0] -= 4
#         # 1번째 칸에 들어감
#         board[1] += 4
#         find_height(index + 1)
#         board[1] -= 4
#         # 2번째 칸에 들어감
#         board[2] += 4
#         find_height(index + 1)
#         board[2] -= 4
#     elif blocks[index] == 2:
#         for k in range(2):
#             if board[k+1] - board[k] > 2:
#                 diff = board[k+1] - board[k]
#                 board[k+1] += 1
#                 board[k] = board[k+1]
#                 find_height(index + 1)
#                 board[k+1] -= 1
#                 board[k] = board[k+1] - diff
#             else:
#                 diff = board[k] - board[k+1]
#                 board[k] += 3
#                 board[k+1] = board[k]
#                 find_height(index + 1)
#                 board[k] -= 3
#                 board[k+1] = board[k] - diff
#             prev_one = board[k]
#             prev_two = board[k+1]
#             next_height = max(board[k], board[k+1])
#             board[k] = next_height + 1
#             board[k+1] = next_height + 3
#             find_height(index + 1)
#             board[k] = prev_one
#             board[k+1] = prev_two
#         next_height = max(board[0]+1, board[1]+1, board[2]+2)
#         prev_zero = board[0]
#         prev_one = board[1]
#         prev_two = board[2]
#         board[0] = board[1] = board[2] = next_height
#         find_height(index + 1)
#         board[0] = prev_zero
#         board[1] = prev_one
#         board[2] = prev_two
#         ####
#         next_height = max(board[0], board[1], board[2])
#         prev_zero = board[0]
#         prev_one = board[1]
#         prev_two = board[2]
#         board[0] = next_height + 2
#         board[1] = next_height + 1
#         board[2] = next_height + 1
#         find_height(index + 1)
#         board[0] = prev_zero
#         board[1] = prev_one
#         board[2] = prev_two
#         #####
#     elif blocks[index] == 3:
#         for k in range(2, 0, -1):
#             if board[k-1] - board[k] > 2:
#                 diff = board[k-1] - board[k]
#                 board[k-1] += 1
#                 board[k] = board[k-1]
#                 find_height(index + 1)
#                 board[k-1] -= 1
#                 board[k] = board[k-1] - diff
#             else:
#                 diff = board[k] - board[k-1]
#                 board[k] += 3
#                 board[k-1] = board[k]
#                 find_height(index + 1)
#                 board[k] -= 3
#                 board[k-1] = board[k] - diff
#             prev_one = board[k]
#             prev_two = board[k-1]
#             next_height = max(board[k], board[k-1])
#             board[k] = next_height + 1
#             board[k-1] = next_height + 3
#             find_height(index + 1)
#             board[k] = prev_one
#             board[k-1] = prev_two
#         next_height = max(board[0]+2, board[1]+1, board[2]+1)
#         prev_zero = board[0]
#         prev_one = board[1]
#         prev_two = board[2]
#         board[0] = board[1] = board[2] = next_height
#         find_height(index + 1)
#         board[0] = prev_zero
#         board[1] = prev_one
#         board[2] = prev_two
#         ####
#         next_height = max(board[0], board[1], board[2])
#         prev_zero = board[0]
#         prev_one = board[1]
#         prev_two = board[2]
#         board[0] = next_height + 1
#         board[1] = next_height + 1
#         board[2] = next_height + 2
#         find_height(index + 1)
#         board[0] = prev_zero
#         board[1] = prev_one
#         board[2] = prev_two
#         #####
#     elif blocks[index] == 4:
#         next_height = max(board[0], board[1], board[2])
#         prev_zero = board[0]
#         prev_one = board[1]
#         prev_two = board[2]
#         board[0] = next_height + 1
#         board[1] = next_height + 2
#         board[2] = next_height + 1
#         find_height(index + 1)
#         board[0] = prev_zero
#         board[1] = prev_one
#         board[2] = prev_two
#         #####
#         next_height = max(board[0]+1, board[1]+2, board[2]+1)
#         prev_zero = board[0]
#         prev_one = board[1]
#         prev_two = board[2]
#         board[0] = next_height
#         board[1] = next_height
#         board[2] = next_height
#         find_height(index + 1)
#         board[0] = prev_zero
#         board[1] = prev_one
#         board[2] = prev_two
#         #####
#         for k in range(2):
#             prev_one = board[k]
#             prev_two = board[k + 1]
#             next_height = max(board[k] + 1, board[k + 1])
#             board[k] = next_height + 2
#             board[k + 1] = next_height + 1
#             find_height(index + 1)
#             board[k] = prev_one
#             board[k + 1] = prev_two
#         for k in range(2, 0, -1):
#             prev_one = board[k]
#             prev_two = board[k - 1]
#             next_height = max(board[k] + 1, board[k - 1])
#             board[k] = next_height + 2
#             board[k - 1] = next_height + 1
#             find_height(index + 1)
#             board[k] = prev_one
#             board[k - 1] = prev_two
#     elif blocks[index] == 5:
#         prev_zero = board[0]
#         prev_one = board[1]
#         prev_two = board[2]
#         next_height = max(board[0], board[1], board[2] - 1)
#         board[0] = next_height + 1
#         board[1] = next_height + 2
#         board[2] = next_height + 2
#         find_height(index + 1)
#         board[0] = prev_zero
#         board[1] = prev_one
#         board[2] = prev_two
#         #####
#         for k in range(2):
#             prev_one = board[k]
#             prev_two = board[k+1]
#             if board[k] - 1 >= board[k+1]:
#                 board[k+1] = board[k] + 1
#                 board[k] += 2
#                 find_height(index + 1)
#                 board[k] = prev_one
#                 board[k+1] = prev_two
#             else:
#                 board[k] = board[k+1] + 3
#                 board[k+1] += 2
#                 find_height(index + 1)
#                 board[k] = prev_one
#                 board[k+1] = prev_two
#     elif blocks[index] == 6:
#         prev_zero = board[0]
#         prev_one = board[1]
#         prev_two = board[2]
#         next_height = max(board[0] - 1, board[1], board[2])
#         board[0] = next_height + 2
#         board[1] = next_height + 2
#         board[2] = next_height + 1
#         find_height(index + 1)
#         board[0] = prev_zero
#         board[1] = prev_one
#         board[2] = prev_two
#         #####
#         for k in range(2, 0, -1):
#             prev_one = board[k]
#             prev_two = board[k - 1]
#             if board[k] - 1 >= board[k - 1]:
#                 board[k - 1] = board[k] + 1
#                 board[k] += 2
#                 find_height(index + 1)
#                 board[k] = prev_one
#                 board[k - 1] = prev_two
#             else:
#                 board[k] = board[k - 1] + 3
#                 board[k - 1] += 2
#                 find_height(index + 1)
#                 board[k] = prev_one
#                 board[k - 1] = prev_two
#     elif blocks[index] == 7:
#         for k in range(2):
#             prev_one = board[k]
#             prev_two = board[k + 1]
#             next_height = max(board[k], board[k+ 1])
#             board[k] = next_height + 2
#             board[k + 1] = next_height + 2
#             find_height(index + 1)
#             board[k] = prev_one
#             board[k + 1] = prev_two
#
#
#
# N = int(sys.stdin.readline())
# blocks = [int(sys.stdin.readline()) for _ in range(N)]
# board = [0, 0, 0]
# result = N * 2
# find_height(0)
# print(result)
'''
10
1
1
1
1
1
1
1
1
1
1

'''


import sys
N = int(sys.stdin.readline())
blocks = [int(sys.stdin.readline()) for _ in range(N)]
possible = []
start = blocks.pop(0)
if start == 1:
    possible.extend([4])
elif start in [2, 3, 4, 5, 6]:
    possible.extend([1, 2, 3])
elif start == 7:
    possible.extend([2])
for block in blocks:
    if block == 1:
        for k in range(len(possible)):
            possible.append(possible[k]+4)
        possible = list(set(possible))
    elif block in [2, 3, 4, 5, 6]:
        for k in range(len(possible)):
            possible.extend([possible[k]+1, possible[k]+2, possible[k]+3])
        possible = list(set(possible))
    elif block == 7:
        for k in range(len(possible)):
            possible.append(possible[k] + 2)
        possible = list(set(possible))
print(sum(possible))
print(len(possible))
print(max(possible)//2)