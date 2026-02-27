#victor Villarreal 
#Practice assignment Ch.3-2 
#last update 2/04/26

#get number in range 

number = int(input('enter a number between 1-7: '))

# print number associated with day 

if number==1:
    print ('Monday')
else:
    if number ==2:
        print ('Tuesday')
    else:
        if number == 3:
            print ('Wednsday')
        else:   
            if number == 4:
                print ('Thursday')
            else: 
                if number == 5:
                    print ('Friday')
                else:
                    if number == 6:
                        print ('Saturday')
                    else:
                        if number == 7:
                            print ('Sunday')
                        else: 
                            if number < 1 or number > 7: 
                                print ("Not in range")
                            
