file_name = 'book.txt'

try:
    input_file = open(file_name, 'r')
except FileNotFoundError: # to fail silently, do pass
    print('file doest not exist in this directory')
    output_file = open(file_name, 'w', encoding = 'UTF-8')
else:
    for line in input_file:
        print(line.rstrip())

input_file = open('random.txt', 'r', encoding = 'UTF-8')
random_lst = input_file.readlines()
output_file.writelines(random_lst)

input_file.close()
output_file.close()

"""
a) print the story (only) to the user
b) count the number of words in the story

1) Make two files cats.txt and dogs.txt. Store at least three names of cats in the
first file and three names of dogs in the second file.
"""

file_name = 'book.txt'

try:
    input_file = open(file_name, 'r')
except FileNotFoundError: # to fail silently, do pass
    print('file doest not exist in this directory')
else:
    word_count = 0
    for line in input_file:
        item = line.rstrip().split()
        print(item)
        word_count += len(item)
    print(input_file)
    print(word_count)
