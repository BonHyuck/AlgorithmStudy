# N = int(input())
# dictionary = {}
# for _ in range(N):
#     text = input()
#     text_key = str(text[0]) + str(text[-1])
#     if dictionary.get(text_key, 0) == 0:
#         dictionary[text_key] = []
#     temp_dict = {}
#     for t in text:
#         temp_dict[t] = temp_dict.get(t, 0) + 1
#     dictionary[text_key].append(temp_dict)
#
# M = int(input())
# for _ in range(M):
#     result = 0
#     text = input()
#     text_key = str(text[0]) + str(text[-1])
#     if dictionary.get(text_key, 0) == 0:
#         print(result)
#         continue
#     for dict in dictionary[text_key]:
#         check = True
#         for letter_key in dict.keys():
#             if dict[letter_key] == text.count(letter_key):
#                 continue
#             else:
#                 check = False
#                 break
#         if check:
#             result += 1
#     print(result)

# 1501. [G5] 영어 읽기
# https://www.acmicpc.net/problem/1501

N = int(input())
# 딕셔너리 형태로 사전 정리
dictionary = {}
# 사전에 있는 단어 등록
for _ in range(N):
    text = input()
    # 단어의 길이가 2 이상
    if len(text) >= 2:
        # 1번째 키 값 생성
        dict_key = text[0] + text[-1]
        # 만일 아직 dict_key에 해당하는 value가 없다면
        if dictionary.get(dict_key, 0) == 0:
            # 해당 key에 value를 빈 딕셔너리로 만들어둔다.
            dictionary[dict_key] = {}
        # 양 끝, key값을 제외한 중간 텍스트를 알파벳순으로 정력
        mid_text = ''.join(sorted(list(text[1:len(text)-1])))
        # dict_key를 1번째 값으로, 정렬된 중간 텍스트를 두번째 key값으로 하여 카운팅
        dictionary[dict_key][mid_text] = dictionary[dict_key].get(mid_text, 0) + 1
    # 단어의 길이가 1
    else:
        # key값은 단어 그 자체
        dict_key = text
        if dictionary.get(dict_key, 0) == 0:
            dictionary[dict_key] = {}
        # 중간 텍스트가 없으므로 빈 문자열을 두번째 key값으로 활용한다.
        dictionary[dict_key][""] = 1

M = int(input())
# 문장 해석 시작
for _ in range(M):
    # 문장의 단어들은 띄어쓰기로 분리돼있다.
    sentence = list(map(str, input().split()))
    # 모든 단어가 사전에 없다면 해석 불가
    no_answer = True
    result = 1
    # 한 문장 내 단어 찾기
    for text in sentence:
        # 위와 같은 맥락으로 딕셔너리 안에 단어를 찾는다.
        if len(text) >= 2:
            dict_key = text[0] + text[-1]
            mid_text = ''.join(sorted(list(text[1:len(text)-1])))
            # 1번째 key값에 해당하는 값이 없다면 끝
            if dictionary.get(dict_key, 0) == 0:
                result *= 1
                continue
            # 2번째 key값에 해당하는 값이 없다면 끝
            if dictionary[dict_key].get(mid_text, 0) == 0:
                result *= 1
                continue
            no_answer = False
            result *= dictionary[dict_key][mid_text]
        else:
            dict_key = text
            if dictionary.get(dict_key, 0) == 0:
                result *= 1
                continue
            no_answer = False
            result *= dictionary[dict_key][""]
    # 문장 내 모든 단어가 사전에 없으면
    if no_answer:
        print("0")
    else:
        print(result)
if N == 0 and M == 0:
    print("0")

