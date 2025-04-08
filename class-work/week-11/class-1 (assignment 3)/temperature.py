# James Ferdinand Combista
# 2438113

def toCelsius(F):
    C = (F - 32)*(5/9)
    return round(C, 2) 

input_file = open('data.txt', 'r')
temp_dict = {}

for line in input_file:
    if line[0][0] == '1': # it's legal
        cleaned_line = line.strip().split()
        values = list(map(float, cleaned_line[1:]))
        temp_dict.update({int(cleaned_line[0]): list(map(toCelsius, values))})

def avgTempYear(dct, year):
    try:
        year_num = dct[year]
    except KeyError:
        print(f'Year {year} is not found in data.')
    else:
        average = round(sum(year_num)/len(year_num), 2)
        return average

def topThreeYears(dct):
    average_lst = []
    three_highest = []

    temperatures = list(dct.keys())
    for temperature in temperatures:
        average_lst.append(avgTempYear(dct, temperature))

    for i in range(3):
        value = max(average_lst)
        three_highest.append(value)
        average_lst.remove(value)
    return three_highest

def avgTempMonth(dct, month):
    month_dict = {'JAN':1, 'FEB': 2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
    total_temp = []
    for year in dct:
        total_temp.append(dct[year][month_dict[month]-1])
    return round(sum(total_temp)/len(total_temp), 2)

input_file.close()