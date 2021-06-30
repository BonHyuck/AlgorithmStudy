goal_count = [2, 3, 5, 7, 11, 13, 17]
A = int(input())
B = int(input())
not_A = 100 - A
not_B = 100 - B
fact = [0, 1]
for k in range(1, 18):
    prev = fact[k]
    next = prev * (k + 1)
    fact.append(next)

result_A = 0
result_B = 0

for goal in goal_count:
    result_A += (fact[18]/(fact[18-goal]*fact[goal]))*(((A / 100) ** goal) * ((not_A / 100) ** (18 - goal)))
    result_B += (fact[18]/(fact[18-goal]*fact[goal]))*(((B / 100) ** goal) * ((not_B / 100) ** (18 - goal)))

result = (result_A + result_B) - (result_A * result_B)

print(result)