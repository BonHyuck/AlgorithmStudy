# 5052. [G4] 전화번호 목록
# https://www.acmicpc.net/problem/5052

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [input() for _ in range(N)]
    # 정렬을 하게 되면 앞에 나올 수 있는 숫자가 앞으로 오게 된다.
    arr = sorted(arr)
    result = "YES"
    for i in range(N - 1):
        text = arr[i]
        next_text = arr[i + 1]
        # 뒤에 있는 전화번호의 길이가 더 크다면
        # (같은 번호는 안 나온다고 했으니까)
        # 앞에 있는 전화번호가 뒤에 있는 전화번호의 앞부분에 나오는지 확인
        if len(text) < len(next_text):
            if next_text[0:len(text)] == text:
                result = "NO"
                break
        else:
            continue
    print(result)