# Question 1
'''
From your accounts.txt file (from last class) read each line and create 
a dictionary of dictionaries.  The outer dictionary key is the account 
number.  The inner dictionary key is the last name and the value in 
the inner dictionary is the balance.  Print the final dictionary.  
'''

accounts_dict = {}

output_file = open('accounts.txt', 'r')
for line in output_file:
        account_number, last_name, balance = line.strip().split()

        account_number = str(account_number)
        
        balance = float(balance)

        if account_number not in accounts_dict:
            accounts_dict[account_number] = {}

        accounts_dict[account_number][last_name] = balance
output_file.close()

#print(accounts_dict)


# Question 2
'''
(a) Open a file called grades.txt for writing that will hold student 
    grade information.  This information will be read from the user.  
    Each input line given by the user is of the form: 
    firstname, lastname, exam1grade, exam2grade, exam3grade.  
    Read grade information for 10 students and write that information 
    to your grades.txt file.  Make sure to close the file after 
    writing to it.  

(b) Once your grades.txt file is populated, read and store the infomration
    from the file.  Determine what data structure (e.g. lists, dictionaries, 
    sets, etc.) would best suit for storing the data in the file.  Once 
    your data is stored, compute the following: 
    (i) the minimum, maximum and average of exam1grade, exam2grade, exame3grade
        for each student and print this information
    (ii) the minimum, maximum and average of exam1grade across all students.
         Do this for exam2grade and exam3grade as well.  
    (iii) the average of the average of all 3 exams for all students.  
'''

students = []

file = open("grades.txt", "r") 

def grades_desc(student):
    exam1 = student['exam1grade']
    exam2 = student['exam2grade']
    exam3 = student['exam3grade']
    
    
    min_grade = min(exam1, exam2, exam3)
    max_grade = max(exam1, exam2, exam3)
    avg_grade = (exam1 + exam2 + exam3) / 3
        
    print(f"Student: {student['firstname']}{student['lastname']}")
    print(f"Minimum grade: {min_grade}")
    print(f"Maximum grade: {max_grade}")
    print(f"Average grade: {avg_grade:.1f}")

for line in file:
    data = line.strip().split(',')

    student = {
        'firstname': data[0],
        'lastname': data[1],
        'exam1grade': float(data[2]),
        'exam2grade': float(data[3]),
        'exam3grade': float(data[4])
        }
    grades_desc(student)

    students.append(student)

global_avr = []
for i in range(3):
    grades = [student[f'exam{i+1}grade'] for student in students]
    min_grade = min(grades)
    max_grade = max(grades)
    avg_grade = sum(grades) / len(grades)
    global_avr.append(avg_grade)

    print(f"Exam {i+1} - Min: {min_grade}, Max: {max_grade}, Avg: {avg_grade:.1f}")

print(f"Average of averages: {sum(global_avr) / len(global_avr):.1f}")

# Question 3
'''
Download into your folder the words.txt file on Lea.  You will notice that each
word in the words.txt file is on a new line.  
(a) Open a new file called words_updated.txt with writing mode, and write all the
    words from the words.txt file continuously one after the other only separated
    by a space.  Make sure that you strip all the white space after each word
    that you read from the words.txt file.  Once you are done, make sure you
    close all files that you had opened.  

(b) Create an integer num_words that will hold the number of words that you have
    in your words_updated.txt (or words.txt) file.  Now prompt the user to read
    an integer k (between 1 and 80) from the user.  Make sure to do input 
    validation so to be assured that the user abides the constraints on k.  

    Open a new file called result.txt with writing mode, and read the words 
    from your words_updated.txt file and write them in result.txt such that
    the number of characters on each line of result.txt is at most k (not
    counting the spaces between the words).  That is, if the next word 
    begin considered fits on the current line, add it to the current line
    (make sure to include a space between each pair of words on the line). 
    Otherwise, put this word on a new line (which will become the new
    current line).

    One you finish writing to your result.txt file, print the content of
    your file.  Make sure to close all files that you have opened.  
'''
input_file = open('words.txt', 'r')
output_file = open('words_updated.txt', 'w')

for line in input_file:
    word = line.rstrip()
    output_file.write(word + ' ')
input_file.close()     
output_file.close()

output_file = open('words_updated.txt', 'r')
num_words = 0

for line in output_file:
    word = line.split()
    num_words += len(word)

k = int(input("Enter an integer k (between 1 and 80): "))
if k < 1 or k > 80:
    print("Invalid input. k must be between 1 and 80.")
    exit()

output_file.close()

output_file = open('result.txt', 'w')
input_file = open('words_updated.txt', 'r')

for line in input_file:
    word_lst = line.split()

line = ''
exclude = ['.', '&', '(', ')']
for word in word_lst:
    if len(word) + len(line) - line.count(' ') <= k and word not in exclude:
        line += word + ' '
    elif line:
        output_file.write(line + '\n')
        line = ''

output_file.close()
input_file.close()