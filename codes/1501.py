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

'''
3
aBABa
aabba
abcaa
2
ababa
abbaa

'''

N = int(input())
dictionary = {}
for _ in range(N):
    text = input()
    if len(text) >= 2:
        dict_key = text[0] + text[-1]
        if dictionary.get(dict_key, 0) == 0:
            dictionary[dict_key] = {}
        mid_text = ''.join(sorted(list(text[1:len(text)-1])))
        dictionary[dict_key][mid_text] = dictionary[dict_key].get(mid_text, 0) + 1
    else:
        dict_key = text
        if dictionary.get(dict_key, 0) == 0:
            dictionary[dict_key] = {}
        dictionary[dict_key][""] = 1

M = int(input())
result_list = []
for _ in range(M):
    sentence = list(map(str, input().split()))
    no_answer = True
    result = 1
    for text in sentence:
        if len(text) >= 2:
            dict_key = text[0] + text[-1]
            mid_text = ''.join(sorted(list(text[1:len(text)-1])))
            if dictionary.get(dict_key, 0) == 0:
                result *= 1
                continue
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
    if no_answer:
        print("0")
    else:
        print(result)
if N == 0 and M == 0:
    print("0")

