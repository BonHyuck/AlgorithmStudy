def solution(n):
    answer = ''
    while n:
        if n % 3 == 0:
            answer = '4' + answer
            n -= 1
        elif n % 3 == 1:
            answer = '1' + answer
        elif n % 3 == 2:
            answer = '2' + answer
        n //= 3

    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))
print(solution(11))
print(solution(12))
