'''
2 3 10
10 15 15
13 11 20
'''


import sys

N, D, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(arr)