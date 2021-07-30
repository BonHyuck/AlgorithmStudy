# 1132. [G3] 합
# https://www.acmicpc.net/problem/1132

N = int(input())
alphabets = [["A", 0], ["B", 0], ["C", 0], ["D", 0], ["E", 0], ["F", 0], ["G", 0], ["H", 0], ["I", 0], ["J", 0]]
texts = []
for k in range(N):
    text = input()
    texts.append(text)
    for tndex in range(len(text)):
        c = text[tndex]
        index = len(text) - tndex
        for k in range(10):
            if alphabets[k][0] == c:
                alphabets[k][1] += (10 ** index)

alphabets = sorted(alphabets, key=lambda x: x[1], reverse=True)
alpha_dict = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0
}
for i in range(10):
    alpha_dict[alphabets[i][0]] = 9 - i

result = 0

for text in texts:
    number = 0
    for t in range(len(text)):
        number += alpha_dict[text[t]] * (10 ** (len(text) - 1 - t))
    result += number

print(result)
