#Victor Villarreal
#
#

import random 

def rando():
    try:
        infile= open('random_nums','w')

        user_nums= int(input('How many whole numbers (1-500) should be in random_nums file: '))

        for lines in range(user_nums):
            infile.write (f'{str(random.randint(1,500))}\n')
    
    
    except ValueError:
        print ('must be WHOLE number within the range 1-500')
    except IOError:
        print ('could not be performed because of I/O')
    
    infile.close

def rando2():
    
    infile =open ('random_nums','r')
    
    #accumilators for counting numbers and lines that numbers are written on 
    line_count= 0
    total = 0 

    #loop that counts numbers and lines after each iteration/line in file
    for lines in infile:
        line_count+= 1
        total+= int(lines)
    
    avg = total/line_count   
    
    print (f'Sum of Integers is: {total}')
    print (f'Average of integers: {avg}')
    print (f'Integers in file: {line_count}')
    
    

    infile.close
    
rando2()