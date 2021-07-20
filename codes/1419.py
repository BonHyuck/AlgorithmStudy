'''
11
30
4
'''

left = int(input())
right = int(input())
k = int(input())
result = 0
# 숫자 = 2x + d
# 3부터 전부 가능
if k == 2:
    if right < 3:
        result = 0
    elif left > 3:
        result = right - left + 1
    else:
        result = right - 3 + 1
# 숫자 = 3x + 3d = 3(x + d)
# 범위 안에서 6보다 크거나 같은 3의 배수
elif k == 3:
    if right < 6:
        result = 0
    elif left <= 6:
        result = right // 3 - 1
    else:
        result = right // 3 - left // 3
        if right % 3 == 0 or left // 3 == 0:
            result += 1
# 숫자 = 4x + 6d = 4(x + d) + 2d
# 범위 안에서 10보다 크거나 같으면서 4로 나눴을때 나머지가 0 혹은 2
# 근데 12는 안됨ㅋ
# 10, 14, 16, 18, 20, ...
elif k == 4:
    if right >= 10:
        if left < 10:
            left = 10
        result = (right - left) // 2 + 1
        if 12 >= left and 12 <= right:
            result -= 1
    else:
        result = 0
# 숫자 = 5x + 10d = 5(x + 2d)
# 15부터 시작하는 5의 배수
elif k == 5:
    if right < 15:
        result = 0
    elif left <= 15:
        result = right // 5 - 2
    else:
        result = right // 5 - left // 5
        if right % 5 == 0 or left // 5 == 0:
            result += 1

print(result)




