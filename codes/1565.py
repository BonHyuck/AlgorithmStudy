def find_gcd(a, b):
    if a % b == 0:
        return b
    return find_gcd(b, a % b)

def find_product(arr):
    number = 1
    for n in arr:
        number *= n
    return number

D, M = map(int, input().split())
# 해당 배열의 최소공배수 구해야함
D_arr = list(map(int, input().split()))
# 해당 배열의 최대공약수 구해야함
M_arr = list(map(int, input().split()))
D_gcd = D_arr[0]
D_lcm = D_arr[0]
M_gcd = M_arr[0]
if D > 1:
    for k in range(1, D):
        D_gcd = find_gcd(D_gcd, D_arr[k])
    D_lcm = find_product(D_arr) // D_gcd
if M > 1:
    for k in range(1, M):
        M_gcd = find_gcd(M_gcd, M_arr[k])

result = 0
for x in range(D_lcm, M_gcd + 1, D_lcm):
    if M_gcd % x == 0:
        result += 1



# print(D_lcm, M_gcd)
print(result)