# def solution(scoville, K):
#     answer = 0
#
#     while len(scoville) > 1:
#         first = scoville.pop(scoville.index(min(scoville)))
#         second = scoville.pop(scoville.index(min(scoville)))
#         number = first + (second * 2)
#         answer += 1
#         if number >= K:
#             # 전부 확인
#             for food in scoville:
#                 if food < K:
#                     break
#             else:
#                 break
#         scoville.append(number)
#
#     # 마지막 확인
#     for food in scoville:
#         if food < K:
#             answer = -1
#             break
#
#     return answer

import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        except:
            answer = -1
            break
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))