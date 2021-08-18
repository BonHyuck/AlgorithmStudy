'''
5
Ab3bd
'''
N = int(input())
text = list(input())
result = N - 1
index_dict = {}
for k in range(N):
    if index_dict.get(text[k], 0) == 0:
        index_dict[text[k]] = [k]
    else:
        index_dict[text[k]].append(k)
for center in range(1, N):
    cnt = 0
    for arr in index_dict.values():
        if len(arr) == 1:
            cnt += 1
            continue
        for i in range(len(arr) // 2):
            if arr[i] > center:
                cnt += 2
            elif arr[i] == center:
                cnt += 1
            else:
                diff = center - arr[i]
                next_idx = center + diff
                if next_idx < N and text[arr[i]] != text[next_idx]:
                    cnt += 1
            if cnt > result:
                break
        if cnt > result:
            break

    if cnt < result:
        result = cnt
print(result)
print(index_dict)
print(text)