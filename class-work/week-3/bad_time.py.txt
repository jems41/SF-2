'''
Given the current time (integer hour, integer min) and 
    the wait time (integer hour, integer min)
    compute the the final time after the wait.
'''

current_hour, current_min = input("Current time? ")
wait_hour, wait_min = input("Wait time? ")

min = current_min + wait_min  
final_time_hour = current_hour + wait_hour 

print(f'The time after waiting is: {final_time_hour}h{min}')