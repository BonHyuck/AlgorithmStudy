# def solution(k, room_number):
#     answer = []
#
#     temp_dict = {}
#
#     for i in range(len(room_number)):
#         number = room_number[i]
#         while True:
#             if temp_dict.get(number, -1) == -1:
#                 temp_dict[number] = 1
#                 answer.append(number)
#                 break
#             else:
#                 number += 1
#
#     return answer

def solution(k, room_number):
    answer = []

    temp_dict = {}

    for i in room_number:
        number = i
        temp = [number]
        while number in temp_dict:
            number = temp_dict[number]
            temp.append(number)
        answer.append(number)
        for k in temp:
            temp_dict[k] = number + 1
    return answer


print(solution(10, [1,3,4,1,3,1]))

