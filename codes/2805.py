# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# # trees = list(map(int, sys.stdin.readline().split()))
# trees = [k * 100000 for k in range(N)]
# tall = max(trees)
# short = min(trees)
# cut = 0
# result = 0
# while True:
#     if tall == short:
#         result = tall
#         break
#     height = (tall + short) // 2
#     for tree in trees:
#         if tree - height >= 0:
#             cut += (tree - height)
#         else:
#             continue
#     if cut > M:
#         short = height
#         cut = 0
#     elif cut < M:
#         tall = height
#         cut = 0
#     else:
#         result = height
#         break
#     if tall == short:
#         result = tall
#         break
# print(result)

N, M = map(int, input().split())
trees = list(map(int, input().split()))
# trees = [k * 100000 for k in range(N)]
tall = max(trees)
short = 1
while short <= tall:
    height = (tall + short) // 2
    cut = 0
    for tree in trees:
        if tree >= height:
            cut += tree - height
    if cut >= M:
        short = height + 1
    else:
        tall = height - 1

print(tall)