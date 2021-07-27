minsik = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']

N = int(input())
texts = [input() for _ in range(N)]
result = []

for index in range(N):
    text = texts[index]
    to_number = []
    tndex = 0
    while tndex < len(text):
        if text[tndex] == 'n':
            if tndex + 1 < len(text):
                if text[tndex + 1] == 'g':
                    to_number.append(minsik.index('ng'))
                    tndex += 2
                    continue
        to_number.append(minsik.index(text[tndex]))
        tndex += 1
    # print(to_number, index)
    result.append((index, to_number))
result = sorted(result, key=lambda x:x[1])
for index, arr in result:
    print(texts[index])

