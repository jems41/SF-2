print('You are to enter two numebers, which I will divide for you ')
print('Enter \'q\' anytime to quit.')

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break

    second_number = input('\nSecond number: ')
    if second_number == 'q':
        break

    try:
        result = int(first_number)/int(second_number)
    except ZeroDivisionError: # if try fails then what happens
        print('cannot divide by 0!')
    except ValueError:
        print('enter an integer for both numbers')
    else: # if try works
        print(f'result is: {result}')
    finally: # will always run
        print('done!')