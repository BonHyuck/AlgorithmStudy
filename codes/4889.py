# 4889. [S1] 안정적인 문자열
# https://www.acmicpc.net/problem/4889

import sys

T = 1
# 계속 돈다
while True:
    # 텍스트 받아오기
    text = sys.stdin.readline()
    # 스택
    stack = []
    # 결과값
    result = 0
    # - 가 있는 문자가 입력값으로 들어오면 종료
    if '-' in text:
        break
    # 종료가 안됐으면 괄호 확인
    for c in text:
        # 여는 괄호는 스택에 넣어준다
        if c == "{":
            stack.append(c)
        # 닫는 괄호가 나온다면?
        elif c == "}":
            # 1. 스택에 아무것도 없으면 닫는 괄호를 여는 괄호로 바꿔줘야한다.
            if len(stack) == 0:
                stack.append("{")
                result += 1
            # 2. 스택의 맨 마지막이 여는 괄호라면 짝이 맞으니까 빼준다.
            elif stack[-1] == '{':
                stack.pop(-1)
    # 닫힌 괄호에서 바뀐 수 + 현재 스택에 남아있는 여는 괄호의 수의 절반(절반만 닫힌 괄호로 바꿔주면 된다.)
    print("{}. {}".format(T, result + len(stack) // 2))
    T += 1