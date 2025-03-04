f, d = input().split()
f = int(f)
d = int(d)
 
days = []
for j in range(d):     
    days.append([int(x) for x in input().split(' ')])

bonus = 0

for i in range(d):
    sums = days[i]
    sum_days = sum(sums)
    if sum_days % 13 == 0:
        bonus += sum_days // 13 

for i in range(f):
    franchiseTotal = []
    for j in range(d):
        franchiseTotal.append(days[j][i])
    sum_franchise = sum(franchiseTotal)
    if sum_franchise % 13 == 0:
        bonus += sum_franchise // 13 

print(bonus)