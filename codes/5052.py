T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [input() for _ in range(N)]
    arr = sorted(arr)
    result = "YES"
    for i in range(N - 1):
        text = arr[i]
        next_text = arr[i + 1]
        if len(text) < len(next_text):
            if next_text[0:len(text)] == text:
                result = "NO"
                break
        else:
            continue
    print(result)