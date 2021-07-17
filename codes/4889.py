import sys

T = 1
while True:
    text = sys.stdin.readline()
    stack = []
    result = 0
    if '-' in text:
        break
    for c in text:
        if c == "{":
            stack.append(c)
        elif c == "}":
            if len(stack) == 0:
                stack.append("{")
                result += 1
            elif stack[-1] == '{':
                stack.pop(-1)
    print("{}. {}".format(T, result + len(stack) // 2))
    T += 1