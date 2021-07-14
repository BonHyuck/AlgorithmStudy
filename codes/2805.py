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

# 2805. 나무 자르기(S3)
# https://www.acmicpc.net/problem/2805

# 주어지는 나무의 수, 가져가려는 나무의 길이
N, M = map(int, input().split())
# 나무들
trees = list(map(int, input().split()))
# 가장 큰 나무 = 절단기 높이의 최대치
tall = max(trees)
# 절단기 최소높이 = 1. 모든 나무를 절단할 수 있는 높이
short = 1
# 이분 탐색으로 값을 찾는다.
while short <= tall:
    # 기준점 = 최대와 최소의 중간점
    # 절단기의 현재 높이
    height = (tall + short) // 2
    # 잘린 나무 총합 = 나무의 윗부분
    cut = 0
    # 절단 시작
    for tree in trees:
        # 나무가 절단기의 높이보다 커서
        # 절단 진행
        if tree >= height:
            cut += tree - height
    # 잘린 나무가 가져가야할 나무보다 많으면
    # 절단기의 높이를 높여서 덜 자르게끔 만든다
    if cut >= M:
        short = height + 1
    # 잘린 나무가 가져가야할 나무보다 적으면
    # 절단기의 높이를 낮춰서 더 자르게끔 만든다
    else:
        tall = height - 1

print(tall)