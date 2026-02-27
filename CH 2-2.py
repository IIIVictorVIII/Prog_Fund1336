#Victor Villarreal 
#Practice assignment Ch.2-2
#last updated 1/29/26

#input monthly gross pay and deductions 

gross_monthly = float(input('Gross monthly income '))
deductions = float(input('Monthly paycheck deductions '))

#calculate and display net monthly 

net_monthly = gross_monthly - deductions 

print (f'Monthly net income is:${net_monthly:,.2f}')

#Calculate yearly gross and net pay 

yearlyNet = net_monthly * 12
yearlyGross = gross_monthly * 12

print (f'yearly gross is:${yearlyGross:,.2f}')
print (f'yearly net is:${yearlyNet:,.2f}')


#hello


