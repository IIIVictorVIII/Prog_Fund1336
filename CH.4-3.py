#Victor Villarreal 
#creates square shape with users suggested character 
#last update 2/10/26

#get user character and dimensions 
character = input('What would you like to make a square with: ')
dimension= int(input('How big should square be (no greater than 15): '))

#validation loop 
while dimension >15:
    print('error: no number greater than 15')
    dimension = int(input('what would you like to make a square with: '))

#produces square shape
for col in range(dimension) :
    for row in range (dimension):
        print (character, end='')
    print ()

    
        
    
    

