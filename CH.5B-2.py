#Victor Villarreal
#Incomplete
#program calculates area of square based on randomly generated integer

import random
import square

side = random.randint(1,100)

def main():
    print('Side:', side)
    print('Area:',square.square_area(side))
    print('Perimeter:',square.square_perimeter(side))

main()
