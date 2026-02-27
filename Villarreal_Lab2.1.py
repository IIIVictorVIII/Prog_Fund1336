#Victor Villarreal 
#completed 1/30/26

'''[ this program calculates ingredients needed to make 
spaghetti sauce based on user input of number of servings]'''

#calculate ammount for one serving
BASE_SERVINGS = 4
TOMATO_SAUCE= 2 / BASE_SERVINGS
TOMATO_PASTE = .3333333 /BASE_SERVINGS
GARLIC_CLOVES= 2 /BASE_SERVINGS
TSP_OREGANO= 1 /BASE_SERVINGS

#user input for desired serving amount 

servings = float(input('Enter the number of servings of spaghetti sauce you want to make '))
 
 #multiply single serving by user input and print results

print (f'to make {servings} servings you will need:')
print (f'{TOMATO_SAUCE * servings: .2f} cups of tomato sauce')
print (f'{TOMATO_PASTE * servings: .2f} cups of tomato paste')
print (f'{GARLIC_CLOVES * servings: .2f} cloves of garlic')
print (f'{TSP_OREGANO * servings: .2f} tablespoons of oregano')