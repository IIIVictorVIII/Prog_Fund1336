#Victor Villarreal 
#Shows how much water level will have risen each year for 25 years
#complete


#constants
RISE_RATE= 1.8
CURRENT_LVL= 0

#headings 
print ('Year\t\tRise (in millimeters)')
print ('-----------------------------')

#loop that prints years and current water lvl
for yrs in range (1,26):
    CURRENT_LVL+=RISE_RATE
    print (f'{yrs}\t\t\t{CURRENT_LVL:.2f}')

