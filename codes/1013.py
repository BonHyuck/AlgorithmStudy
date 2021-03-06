# import re
#
# T = int(input())
# for test_case in range(T):
#     text = input()
#     if re.fullmatch('(100+1+|01)+', text) is not None:
#         print("YES")
#     else:
#         print("NO")

# 1013. [G5] Contact
# https://www.acmicpc.net/problem/1013

import sys
import re

N = int(sys.stdin.readline())
for _ in range(N):
    text = sys.stdin.readline()
    if re.fullmatch('(100+1+|01)+', text) is not None:
        print("YES")
    else:
        print("NO")