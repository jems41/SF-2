villagesAmount = int(input())
villages = []

for i in range(villagesAmount):
    village = int(input())
    villages.append(village)

villages.sort()

sizes = []
for i in range(villagesAmount-1):
    average = (villages[i+1] - villages[i])/2 + villages[i]
    sizes.append(average)

idk = [] 
for i in range(len(sizes)-1):
    idk.append(sizes[i+1] - sizes[i])

print(min(idk))