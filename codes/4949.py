while True:
    text = input()
    if text == ".":
        break
    stack = []
    for char in text:
        if char == "(" or char == "[":
            stack.append(char)
        if len(stack) == 0 and (char == ")" or char == "]"):
            stack.append(char)
            break
        if char == ")" and stack[-1] == "(":
            stack.pop(-1)
        elif char == ")" and stack[-1] != "(":
            stack.append(char)
            break
        if char == "]" and stack[-1] == "[":
            stack.pop(-1)
        elif char == "]" and stack[-1] != "[":
            stack.append(char)
            break
    if len(stack) > 0:
        print("no")
    else:
        print("yes")
