N, A, B = map(int, input().split())
rounds = 0
while True:
    rounds += 1

    if A % 2:
        A //= 2
        A += 1
    else:
        A //= 2

    if B % 2:
        B //= 2
        B += 1
    else:
        B //= 2

    if A == B:
        break

print(rounds)