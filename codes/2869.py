# A, B, V = map(int, input().split())
# moved = 0
# days = 0
# while moved < V:
#     days += 1
#     moved += A
#     if moved >= V:
#         break
#     moved -= B
# print(days)

A, B, V = map(int, input().split())
V -= A
days = V // (A-B)
if V % (A-B) > 0:
    days += 2
else:
    days += 1
print(days)