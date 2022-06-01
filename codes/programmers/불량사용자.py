# import re
#
#
# def solution(user_id, banned_id):
#     answer = 0
#     cnt_arr = [0 for _ in range(len(banned_id))]
#
#     for idx, check_name in enumerate(banned_id):
#         check_name = check_name.replace("*", ".")
#         pattern = re.compile(check_name)
#         for user in user_id:
#             try:
#                 start, end = pattern.fullmatch(user).span()
#                 if start == 0 and end == len(user):
#                     cnt_arr[idx] += 1
#             except:
#                 continue
#
#     return answer

from itertools import permutations
import re

def solution(user_id, banned_id):
    possible = list(permutations(user_id, len(banned_id)))
    result_set = set()

    for users in possible:
        for idx, ban in enumerate(banned_id):
            ban = ban.replace("*", ".")
            pattern = re.compile(ban)
            try:
                start, end = pattern.fullmatch(users[idx]).span()
                if start == 0 and end == len(ban):
                    continue
            except:
                break
        else:
            result_set.add(tuple(sorted(list(users))))

    return len(result_set)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))