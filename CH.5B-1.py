#Victor Villarreal 
#Complete
#program generates a random floating points number between 1-100 for radius 
#then uses radius to solve area of circle 

import random
import math

radius = random.uniform (1,100)

def main():
    print(f'Radius:{radius:.2f}')
    print(f'Area: {area_calc(radius):.2f}')

def area_calc(x):
    area = math.pi * x**2
    return area

main()


