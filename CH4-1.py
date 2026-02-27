#Victor Villarreal 
#While loop that adds two numbers from the users 
#last update 2/10/26

#loop variable
looping = 'y'

#asks user for numbers and adds them 

print ('I can add any two numbers')

while looping == 'y':
    FN = int(input('Give me first number: '))
    SN =int(input('Give me second number: '))
    print (FN + SN)
    
    #reassigns looping to see weather program should repeat
    looping = input('Would you like to try again, y or n? ')

