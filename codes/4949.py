# 4949. 균형잡힌 세상(S4)
# https://www.acmicpc.net/problem/4949

while True:
    text = input()
    if text == ".":
        break
    stack = []
    # 문자 하나하나 검사
    for char in text:
        # 왼쪽 괄호라면 stack에 넣어주기
        if char == "(" or char == "[":
            stack.append(char)
        # stack에 아무것도 없는데 오른쪽 괄호가 나오면
        # => 짝이 안맞으므로 종료
        if len(stack) == 0 and (char == ")" or char == "]"):
            stack.append(char)
            break
        # 오른쪽 괄호가 나왔으며 짝이 맞는 왼쪽 괄호가 stack의 끝에 있을때
        # 왼쪽 괄호를 빼준다.
        if char == ")" and stack[-1] == "(":
            stack.pop(-1)
        # 오른쪽 괄호가 나왔지만 왼쪽 괄호가 stack의 끝에 없다면
        # => 짝이 안맞으므로 종료
        elif char == ")" and stack[-1] != "(":
            stack.append(char)
            break
        # 오른쪽 괄호가 나왔으며 짝이 맞는 왼쪽 괄호가 stack의 끝에 있을때
        # 왼쪽 괄호를 빼준다.
        if char == "]" and stack[-1] == "[":
            stack.pop(-1)
        # 오른쪽 괄호가 나왔지만 왼쪽 괄호가 stack의 끝에 없다면
        # => 짝이 안맞으므로 종료
        elif char == "]" and stack[-1] != "[":
            stack.append(char)
            break
    # 짝이 맞는 경우 전부 빼줬으므로
    # stack이 비어있지 않는 경우 짝이 맞지 않는다.
    if len(stack) > 0:
        print("no")
    else:
        print("yes")
