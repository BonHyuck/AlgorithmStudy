# 1188. [G5] 음식 평론가
# https://www.acmicpc.net/problem/1188

def find_gcd(sausage, person):
    # 소시지를 공평하게 나눠줄 수 있다.
    if sausage % person == 0:
        return person
    return find_gcd(person, sausage % person)


# N = 소시지
# M = 평론가
N, M = map(int, input().split())
print(M - find_gcd(N, M))
