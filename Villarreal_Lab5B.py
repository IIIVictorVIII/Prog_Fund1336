#victor Villarel
#complete
#program projects distance for fallen object from 1-10 seconds 


import distance

#headers
print('time\tfalling distance')
print('________________________')

#puts falling distance function in loop causing it to use each iteration as seconds 
#for distance calculation
def main():
    for seconds in range (1,11):
        print(seconds, '\t', f'{distance.falling_distance(seconds):.2f}')

main()
