#Victor Villarreal 
#2 loop sytem that the user sets parameters for 
#Last update 2/10/26

startingNum = int(input('what is a low number: '))
endingNum = int(input('what is a high number: '))
print()

#produces list with users suggested range numbers x 10 
print('Number\tNumbersx10')
print('------------------')
for number in range (startingNum, endingNum + 1) :
    userNum= number*10
    print (number, '\t',userNum)

#produces count of values in between user low to their high 
print()
total= 0.0                                  #accumulator
print('count in between is:')
print('--------------------')
for count in range (startingNum, endingNum +1):
    total += count 
print (total)