# 피보나치 배열 넉넉하게 잡아두기
fibo = [0 for _ in range(45)]
# 초기값 설정
fibo[0] = 0
fibo[1] = 1
# 두개의 값은 있으니 시작값 = 2
index = 2
# 끝까지
while index < 45:
     fibo[index] = fibo[index-1] + fibo[index-2]
     index += 1

# 위의 방식대로 진행한 이유는
# 0과 1의 개수도 피보나치의 규칙을 따르기 때문
# 따라서 피보나치 배열만 만들고 적절한 값을 가져오면
# 답이 된다.

# 아래의 number가 0일 경우 대비
fibo[-1] = 1

T = int(input())
for test_case in range(1, T+1):
    number = int(input())

    print('{} {}'.format(fibo[number-1], fibo[number]))