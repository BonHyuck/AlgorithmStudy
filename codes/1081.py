L, U = map(int, input().split())
U_total = 0
U_cnt = [0 for _ in range(10)]
cnt_ten = 0
while U > 0:
    val = U // (10 ** cnt_ten)
    rest = U % (10 ** cnt_ten)
    for k in range(10):
        U_cnt[k] += val * cnt_ten
        if k <= rest // (10 ** cnt_ten):
            U_cnt[k] += (10 ** cnt_ten)

