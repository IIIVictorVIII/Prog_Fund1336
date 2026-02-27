#Victor Villarreal 
#Practice assignment Ch. 2-1
#last update 1/29/26

#Asking for price of items 

Hamburger_Price = float(input("Hamburger cost? "))
Fries_Price = float(input("Fries cost? " ))
Shake_Price = float(input("Shake cost? "))

#calc average and total 

total = Hamburger_Price + Fries_Price + Shake_Price
Avg = total /3

#print both avg and total 

print (f'The cost is ${total:.2f}')
print (f'The average cost is ${Avg:.2f}')
