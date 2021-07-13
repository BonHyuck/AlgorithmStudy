# 1341. 사이좋은 형제(G3)
# https://www.acmicpc.net/problem/1341

from fractions import Fraction

A, B = map(int, input().split())
youngsik = Fraction(A, B)
minsik = 1 - youngsik

# 영식이 혼자 다 먹음
if A == B:
    print('*')
# 민식이 혼자 다 먹음
elif A == 0:
    print('-')
else:
    # 패턴이 반복되면서 비율은 유지
    ratio = youngsik / minsik
    swap = False
    if ratio < 1:
        ratio = 1 / ratio
        swap = True
        youngsik = minsik
    # 영식이가 먹고 시작
    result = '*'
    # 영식이가 먹어야되는 남은 부분
    youngsik_left = youngsik - Fraction(1, 2)
    # 영식이가 먹은 부분
    youngsik = Fraction(1, 2)
    # 민식이가 먹은 부분
    minsik = 0

    k = 1
    # 최대 60
    while len(result) < 60:
        k += 1
        # 다음 사람이 먹을 케이크의 양
        next_cake = Fraction(1, 2 ** k)
        # 영식이가 더 먹을 수 있으면
        if next_cake <= youngsik_left:
            youngsik += next_cake
            youngsik_left -= next_cake
            result += '*'
        # 민식이 차례
        else:
            minsik += next_cake
            result += '-'
        # 민식이도 케이크를 먹었고, 둘의 비율이 맞아 떨어지면?
        # 민식이가 분모니까 ZeroDivision 방지
        if minsik != 0 and youngsik / minsik == ratio:
            break
    # break가 아닌 조건때문에 반복문이 끝나는 경우
    else:
        result = ''

    # 패턴이 길어져서 끝났음
    if result == '':
        print('-1')
    else:
        # 민식이가 먼저 시작한다면
        if swap:
            # 민식이가 영식이고 영식이가 민식이고
            for i in result:
                if i == '*':
                    print('-', end='')
                else:
                    print('*', end='')
        else:
            print(result)