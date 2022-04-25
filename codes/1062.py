import sys
input = sys.stdin.readline

def find_word(learning, learned):
    global result

    if learned == K:
        temp = 0
        for text in texts:
            for t in text:
                if visited[ord(t) - 97] == 0:
                    break
            else:
                temp += 1
        result = max(result, temp)
        return

    for n in range(learning, 26):
        if not visited[n]:
            visited[n] = 1
            find_word(n, learned + 1)
            visited[n] = 0



N, K = map(int, input().split())
texts = []
result = 0
visited = [0 for _ in range(26)]
visited[ord('a') - 97] = 1
visited[ord('c') - 97] = 1
visited[ord('i') - 97] = 1
visited[ord('n') - 97] = 1
visited[ord('t') - 97] = 1

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    K -= 5
    for k in range(N):
        text = input()
        texts.append(text[4:-5])

    find_word(0, 0)
    print(result)
