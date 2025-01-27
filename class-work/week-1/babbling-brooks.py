specs = []

while True:
    detail = input("Input each details of a stream: (Input 77 for end) ")
    if detail == '77':
        specs.append(int(detail))
        break
    else:
        specs.append(int(detail))

streams = specs[0]

def babbling_brooks(input, streamAmount):
    lst = []
    for i in range(streamAmount):
        lst.append(input[i+1])
    for i in range(len(input)):
        if input[i] == 99:
            stream = input[i+1]-1
            ratio = input[i+2]
            fork1 = lst[stream] * ratio/100
            fork2 = lst[stream] - fork1
            lst.pop(stream)
            lst[stream:stream] = [fork1, fork2]
        if input[i] == 88:
            stream_merge = input[i+1]-1
            merge = lst[stream_merge] + lst[stream_merge+1]
            lst = lst[:stream_merge] + lst[stream_merge+2:]
            lst.insert(stream_merge, merge)
        if input[i] == 77:
            rounded_list = []
            for x in lst:
                rounded_list.append(round(x))
            return rounded_list

print(babbling_brooks(specs, streams))