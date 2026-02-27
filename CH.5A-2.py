#Victor Villarreal 
#complete
#takes users distance in kilometers and converts to miles 

CONVERSION= .6214

#main gets users distances and passes that variable into convert function 
def main ():
    distance= float(input('Enter distance in kilometers:'+ '\n'))
    convert(distance)
    print (f'{distance} kilometers is {convert(distance):.2f} miles')

#convert function takes whatever number is inside of it
# and multiplies it by the conversion factor then displays result    
def convert(num):
    miles = num*CONVERSION
    return miles
    

main()