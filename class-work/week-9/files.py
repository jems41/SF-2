output_file = open('accounts.txt', 'w')

for i in range(5):
    line = input()
    output_file.write(line+'\n')
    
output_file.close()
