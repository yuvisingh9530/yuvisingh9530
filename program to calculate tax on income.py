# Write a program to calculate tax given the following conditions:
#If income is less than 150000 then there is no tax
#If taxable income is 150000 - 300000 then charge 10% tax
#If taxable income is 300000 - 500000 then charge 20% tax 
#if taxable income is above 500000 then charge 30% charge

Min1 = 150001
Max1 = 300000
Rate1 = 0.10
Min2 = 300001
Max2 = 500000
Rate2 = 0.20
Min3 = 500001
Rate3 = 0.30

income = int(input("Enter your income :"))
taxable_income = income - 150000
if(taxable_income <= 0):
    print("No Tax")
elif(taxable_income>=Min1 and taxable_income<Max1):
    tax = (taxable_income - Min1) * Rate1
elif(taxable_income>=Min2 and taxable_income<Max2):
    tax = (taxable_income - Min2) * Rate2
else:
    tax = (taxable_income-Min3)*Rate3
print("Tax = ",{tax})