import json

# deserialization of JSON -> conversion of JSON object to respective Python object
# input_file = open('student.json', 'r')
# data = json.load(input_file)
# print(data)
# print(type(data))
# input_file.close()

input_file = open('student.json', 'r')
for line in input_file:
    print(line)
    print(type(line))

# serialization of JSON -> conversion of Python object to JSON object/string
output_file = open('butterflies.json', 'w')
d = {'painted lady': 1, 'bronze copper': 12, 'monarch': 5}
json.dump(d, output_file)
output_file.close()