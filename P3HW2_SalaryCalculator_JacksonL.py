# CTI 110
# P3HW2 - Salary Calculator
# JacksonLaura
# 11.22.22

# This program calculates whether or not an employee has worked overtime.

employeeName = input('Enter employee name: ')
numHours = int(input('Enter number of hours worked this month: '))
payRate = float(input('Enter employee pay rate: '))

# figure if employee worked overtime
if numHours > 160:
  print('You worked overtime.')
else:
  print('You did not work overtime.')

# need to cap at 160/month, need to add float?
basePay = 160 * payRate
print('Your base pay is $ ', basePay)


# ask for number of overtime hrs

# overtimeHrs = print(int(input('How many hours of overtime did you work? '))) 
print('How many hours of overtime did you work? ')
overtimeHrs = int(input())

#calculate overtime payrate 
overtimeRate = float(payRate * 1.5)
print('Your overtime pay rate is', overtimeRate, 'per hour.')

#calculate overtime pay only
overtimeTotal = float(overtimeRate * overtimeHrs)
print('Your total amount for overtime pay is $ ', overtimeTotal)


# calculate gross pay
grossPay = float(overtimeTotal + basePay)
print('Your total paycheck will be: $ ', grossPay)
