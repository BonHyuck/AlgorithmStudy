N = int(input())
stack = []
for k in range(N):
    number = int(input())
    if number != 0:
        stack.append(number)
    else:
        stack.pop(-1)
print(sum(stack))