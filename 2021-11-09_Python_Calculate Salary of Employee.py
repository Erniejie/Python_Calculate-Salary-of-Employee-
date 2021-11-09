#Calculate Salary of Employee in Python
#Computer Programming Tutor,Nov 8,2021

days = float(input("Enter  Number of days worked:"))
wages = float(input("Enter Wages per day:[£/day]:"))
basic = wages*days
Ho= basic*0.25    # Housing
Tr = basic*0.15   # Transport Bonus
Tax = basic*0.12
net = basic + Ho + Tr - Tax
print("\nBasic:%1f \nHousing:%1f \nTrans.:%1f \nTax:%1f \nNet Salary:%1f" %(basic,Ho,Tr,Tax,net)
    )
