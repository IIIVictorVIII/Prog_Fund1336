#Victor Villlarreal 
#status: complete 
'''program takes number of packages ordered and 
computes discount based on ordered packages then displays
total before and after discount'''




#users packages 
ordered = int(input('How many packages were ordered?: '))

PACKAGE_PRICE = 149
TOTAL = PACKAGE_PRICE * ordered 

#Discount logic 
if ordered >= 10 and ordered <= 49  : 
    discount = .1 
elif ordered>= 50 and ordered <=99:
    discount = .2          
elif ordered>= 100 and ordered<= 149:
    discount = .3
elif ordered>= 150:
    discount= .4
elif ordered <10 :
    discount = 0
dtotal = discount * TOTAL

#print package totals 

print (f'Total after Discount: ${TOTAL - dtotal :,.2f}')
print (f'Total: ${TOTAL:,.2f}')

'''notes: simplify program more, have better sequence '''
