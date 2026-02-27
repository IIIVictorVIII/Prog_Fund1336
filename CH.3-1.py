#Victor Villarreal 
#Practice assignment Ch.3-1 
#last update 2/04/26



#get user date 
Month = int(input(f'what is the month: '))
if Month<1 and Month>12:
        print('invalid month')
        exit ()

Day = int(input('what is the day:'))
if Day< 1 and Day > 31:
        print('invalid day')
        exit ()
        
Year = int(input('what is the year: '))
if Year <0 and Year >99:
        print('invalid year')
        exit ()


#magic date calculation
magicDate = Day * Month


#check if magic date
if magicDate == Year:
    print('This is a magic date!')
else:
    print('This is not a magic date.')
