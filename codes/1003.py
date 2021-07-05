fibo = [0 for _ in range(45)]
fibo[0] = 0
fibo[1] = 1
index = 2
while index < 45:
     fibo[index] = fibo[index-1] + fibo[index-2]
     index += 1

fibo[-1] = 1

T = int(input())
for test_case in range(1, T+1):
    number = int(input())

    print('{} {}'.format(fibo[number-1], fibo[number]))