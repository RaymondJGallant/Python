#Author='RaymondJamesGallant'
#Date && Time ='9/20/2023 11:13
#Title ='A program that converts the hours and wages into the gross pay for an employee'


hours=input('Please give me the amount of hours worked for the pay period ')
wage=input('Please give me the hourly wage ')
gross_pay = float(hours) * float(wage) 

print(gross_pay)
if (gross_pay <= 200):
    print('You need a raise')