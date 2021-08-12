from itertools import permutations

arr = list(input())
if len(arr) == 1:
    print(arr[0])
else:
    result = -1
    for record in permutations(arr, len(arr)):
        prev = ''
        now = record[0]
        for i in range(1, len(record)):
            next_person = record[i]
            if next_person == 'B':
                if now == "B":
                    result = -1
                    break
            elif next_person == 'C':
                if prev == 'C' or now == 'C':
                    result = -1
                    break
            prev = now
            now = next_person
        else:
            result = ''.join(record)
        if result == -1:
            continue
        else:
            break
print(result)