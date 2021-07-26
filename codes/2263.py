import sys
sys.setrecursionlimit(100000)


def find_preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    parent_node = postorder[post_end]
    print(parent_node, end=" ")
    find_preorder(in_start, inorder.index(parent_node) - 1, post_start, post_start + (inorder.index(parent_node) - in_start) - 1)
    find_preorder(inorder.index(parent_node) + 1, in_end, post_start + (inorder.index(parent_node) - in_start), post_end - 1)


N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
root = postorder[-1]
result = []
find_preorder(0, N - 1, 0, N - 1)