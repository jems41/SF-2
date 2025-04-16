import json

# convert from JSON to Python
student_record = '{"name": "Lucy", "year": 1, "college": "Dawson"}' # some .json file
parsed_record = json.loads(student_record)
print(parsed_record) # prints a dictionnary (notice the single quotations)

# convert from Python to JSON
student_dict = {'name': 'Lucy', 'year': 1, 'college': 'Dawson'} # some dictionnary
student_record_json = json.dumps(student_dict)
print(student_record_json) # prints json file (with the double quotations)

print('\n\n')
print(json.dumps({'name': 'Lucy', 'year': 1})) # dict -> JSON object
print(json.dumps(['red', 'green', 'blue', 1])) # list -> array
print(json.dumps(('apple', [1, 2, 3]))) # tuple -> array
print(json.dumps('hello world')) # string -> string
print(json.dumps(12)) # int -> number
print(json.dumps(12.02)) # float -> number
print(json.dumps(True)) # True -> true
print(json.dumps(False)) # False -> false
print(json.dumps(None)) # None -> null