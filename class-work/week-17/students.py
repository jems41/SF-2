import json

def load_students(file_start):
    try:
        file_student = open(file_start, 'r')
    except FileNotFoundError:
        return
    else:
        data = json.load(file_student)
        file_student.close()
        return data

def save_students(filename, data):
    try:
        file_student = open(filename, 'w')
    except FileNotFoundError:
        return
    else:
        json.dump(data, file_student)
        file_student.close()

def add_student(filename, name, age, grades):
    old_lst = load_students(filename)
    new_student = {}
    new_student['name'] = name
    new_student['age'] = age
    new_student['grades'] = grades
    old_lst.append(new_student)
    save_students(filename, old_lst)
    

def get_average_grade(filename, name):
    student_lst = load_students(filename)
    for student in student_lst:
        if name == student['name']:
            avg = sum(student['grades']) / len(student['grades'])
            return avg
    return f'Student {name} not found.'

def main_program():
    while True:
        answer = input('(Add student, Get average grade, or Exit) ')
        if answer == 'Add student':
            name = str(input('name? '))
            age = int(input('age? '))
            grades = []
            for i in range(3):
                grade = int(input(f'grade {i+1}? '))
                grades.append(grade)

            add_student('students.json', name, age, grades)
        elif answer == 'Get average grade':
            name = str(input('name? '))
            print(get_average_grade('students.json', name))
        elif answer == 'Exit':
            return
        else:
            print('Try again!')

main_program()