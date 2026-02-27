#Victor Villarrel 
#helps user budget for the week.
#complete

#variables 
TOTAL= 0
BUDGET = float(input('Amount budgeted for the month: '))
SPENT = float(input('weekly spent (0 to quit): '))

#loop for each week with 0 as sentinal 
while SPENT !=0 :
    TOTAL += SPENT
    SPENT = float(input('Weekly spent(0 to quit): '))


#prints orginal budget plan, total spent, and if the user is over or under budget
print (f'Budgeted: ${BUDGET:.2f}')
print (f'Spent: ${TOTAL:.2f}' )

if TOTAL > BUDGET : 
    print(f'you are ${TOTAL-BUDGET:.2f} over budget. PLAN BETTER NEXT TIME!')
else : 
    print (f'you are ${BUDGET-TOTAL:.2f} under budget. Nice planning!')

