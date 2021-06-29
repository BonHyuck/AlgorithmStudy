def preorder(idx):
    global pre_result

    if len(pre_result) >= N:
        return

    # 아직 방문 안 한 노드
    if visited[idx] == 0:
        # 해당 노드 추가
        pre_result += chr(idx+65)
        # 방문 처리
        visited[idx] = 1
        # 왼쪽 자식으로 이동
        if 1 <= tree[idx][0] <= 26:
            preorder(tree[idx][0])
        # 오른쪽 자식으로 이동
        if 1 <= tree[idx][1] <= 26:
            preorder(tree[idx][1])
    else:
        return


def inorder(idx):
    global in_result

    if len(in_result) >= N:
        return

    # 현재 노드의 왼쪽 자식 있음 + 방문처리 안함
    if 1 <= tree[idx][0] <= 26 and visited[tree[idx][0]] == 0:
        # 왼쪽 자식한테 간다
        inorder(tree[idx][0])

    in_result += chr(idx + 65)
    visited[idx] = 1
    # 오른쪽 자식 있음 + 방문 처리 안함
    if 1 <= tree[idx][1] <= 26 and visited[tree[idx][1]] == 0:
        inorder(tree[idx][1])
    return


def postorder(idx):
    global post_result

    if len(post_result) >= N:
        return

    # 현재 노드의 왼쪽 자식 있음 + 방문처리 안함
    if 1 <= tree[idx][0] <= 26 and visited[tree[idx][0]] == 0:
        # 왼쪽 자식한테 간다
        postorder(tree[idx][0])

    # 현재 노드의 오른쪽 자식 있음 + 방문처리 안함
    if 1 <= tree[idx][1] <= 26 and visited[tree[idx][1]] == 0:
        # 왼쪽 자식한테 간다
        postorder(tree[idx][1])

    post_result += chr(idx + 65)
    visited[idx] = 1


def reset_visited():
    for i in range(N):
        visited[i] = 0


N = int(input())
tree = [(0, 0) for _ in range(N)]
visited = [0 for _ in range(N)]

# 부모를 인덱스로 해서 트리 형성
for k in range(N):
    parent, left, right = map(str, input().split())
    tree[ord(parent) - 65] = (ord(left)-65, ord(right)-65)

# 전위순회 결과
pre_result = ''
# 중위순회 결과
in_result = ''
# 후위순회 결과
post_result = ''
# 전위순회 시작
preorder(0)
reset_visited()
# 중위순회 시작
inorder(0)
reset_visited()
# 후위순회 시작
postorder(0)

print(pre_result)
print(in_result)
print(post_result)
