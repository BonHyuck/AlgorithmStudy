# text = input()
# N = len(text)
# if N == 1:
#     if int(text) < 9:
#         print(int(text) + 1)
#     else:
#         print(11)
# else:
#     result = ''
#     # 길이가 홀수일 때
#     if N % 2 == 1:
#         front = text[0:N // 2]
#         front_reverse = text[N//2 - 1::-1]
#         center = text[N//2]
#         back = text[N - N // 2:]
#         back_reverse = text[:N - N // 2 - 1:-1]
#         # 앞을 뒤집은 수가 뒤의 수보다 크다면
#         # 그냥 넣어주면 됨
#         if int(front_reverse) > int(back):
#             back = front_reverse
#             result = front + center + back
#         # 앞을 뒤집은 수가 뒤의 수보다 작으면
#         else:
#             # 연산시 올림이 있을 예정
#             if int(center) == 9:
#                 front = int(front)
#                 front += 1
#                 front = str(front)
#                 front_reverse = str(front)[::-1]
#                 center = '0'
#             else:
#                 center = int(center)
#                 center += 1
#                 center = str(center)
#             back = front_reverse
#             if center == back[0] and int(center) == 0:
#                 result = front + back
#             else:
#                 result = front + center + back
#     # 길이가 짝수일 때
#     else:
#         front = text[0:N // 2]
#         front_reverse = text[N // 2 - 1::-1]
#         back = text[N - N // 2:]
#         back_reverse = text[:N - N // 2 - 1:-1]
#         # 앞을 뒤집은 수가 뒤의 수보다 크다면
#         # 그냥 넣어주면 됨
#         if int(front_reverse) > int(back):
#             back = front_reverse
#             result = front + back
#         # 앞을 뒤집은 수가 뒤의 수보다 작으면
#         else:
#             front = int(front)
#             front += 1
#             front = str(front)
#             front_reverse = str(front)[::-1]
#             back = front_reverse
#             if front[-1] == back[0] and int(back[0]) == 0:
#                 result = front + back[1:]
#             else:
#                 result = front + back
#
#     print(int(result))

# 1334. 다음 팰린드롬 수(S3)
# https://www.acmicpc.net/problem/1334

text = input()
N = len(text)
if N == 1:
    if int(text) < 9:
        print(int(text) + 1)
    else:
        print(11)
else:
    # 새로 만들 숫자
    number = ""
    # 입력받은 숫자의 앞부분
    front = text[0:N//2]
    # 입력받은 숫자의 앞부분 뒤집은거
    front_reverse = front[::-1]
    # 입력받은 숫자의 길이가 홀수
    if N % 2 == 1:
        # 홀수이기에 가운데값이 있음
        center = text[N//2]
        # 새로운 숫자는 무조건 팰린드롬
        number = front + center + front_reverse
        # 새로 만들어진 팰린드롬 수가 입력 수보다 크면
        # 끝
        if int(number) > int(text):
            print(number)
        # 그게 아니라면
        else:
            # 가운데값이 9보다 작으면
            # 올림 없음
            # 가운데 값 1 올려주고 끝
            if int(center) < 9:
                center = str(int(center) + 1)
                number = front + center + front_reverse
            # 가운데 값이 9라면
            # +1을 했을떄 하나 올라감
            else:
                # 그로 인해 새로운 값이 생겨나고
                new_front = str(int(front) + 1)
                # 연산으로 인해 새로운 값의 길이가 바뀐다면
                # ex) 99 => 100
                if len(new_front) > len(front):
                    # front의 끝이 0이 되면서 길이가 바뀌었기때문에
                    # 가운데값이 필요없이 그대로 진행
                    number = new_front + new_front[::-1]
                else:
                    # 가운데 값이 0이 되면서 숫자 구성
                    number = new_front + "0" + new_front[::-1]
            print(number)
    # 입력받은 숫자의 길이가 짝수
    # 위와 비슷한 로직으로 진행
    else:
        # 가운데 값 없이 진행
        number = front + front_reverse
        if int(number) > int(text):
            print(number)        
        else:
            new_front = str(int(front) + 1)
            if len(new_front) > len(front):
                number = new_front[0:len(new_front) - 1] + new_front[::-1]
            else:
                number = new_front + new_front[::-1]
            print(number)
