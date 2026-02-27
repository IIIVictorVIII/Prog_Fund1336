#Victor Villarreal 
#Assignment: CH.3-2 with elif logic
#last update: 2/10/26

#loop variable 
looping = 'y'

#get number in range 
while looping== 'y':
    number = int(input('pick a number in the range 1-7 '))

#print corresponding day of the week 
    if number==1 :
        print("Monday")
    elif number==2 :
        print ('Tuesday')
    elif number ==3 : 
        print ('Wednsday')
    elif number == 4 :
        print ('Thursday')
    elif number == 5: 
        print ('friday')
    elif number == 6: 
        print ('Saturday')
    elif number == 7 :
        print ('Sunday')
    elif number < 1 or number > 7: 
        print ('not in range')
