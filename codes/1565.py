def find_gcd(a, b):
    if a % b == 0:
        return b
    return find_gcd(b, a % b)

def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

D, M = map(int, input().split())
# 해당 배열의 최소공배수 구해야함
D_arr = list(map(int, input().split()))
# 해당 배열의 최대공약수 구해야함
M_arr = list(map(int, input().split()))
M_gcd = M_arr[0]
for k in range(1, M):
    M_gcd = find_gcd(M_gcd, M_arr[k])

D_lcm = 1
for k in range(D):
    D_lcm = find_lcm(D_lcm, D_arr[k])
    if D_lcm > M_gcd or D_lcm == 0:
        break

result = 0

idx = 1
while idx * idx < M_gcd:
    if M_gcd % idx == 0:
        if idx % D_lcm == 0:
            result += 1
        if (M_gcd // idx) % D_lcm == 0:
            result += 1
    idx += 1

if idx * idx == M_gcd and idx % D_lcm == 0:
    result += 1

# print(D_lcm, M_gcd)
print(result)