def isDistinct(year):
    s = str(year)
    digits_used = []
    for chat in s:
        if chat in digits_used:
            return False
        digits_used.append(chat)
    return True

year = int(input())
year = year + 1

while not isDistinct(year):
    year += 1

print(year)