#taking input of employee details

name=input("Enter employee name: ")
emp_id=input("Enter employee id: ")
basic_monthly_salary=float(input("Enter employee Basic monthly salary: "))
sepcial_allowance=float(input("Enter employee Special Allowance: "))
bonus_per=float(input("Enter employee Bonus percentage: "))/100

#Calculate Gross Monthly Salary
gross_monthly_salary=basic_monthly_salary+sepcial_allowance

#Calculate bonus
bonus=gross_monthly_salary*bonus_per*12

#Calculate Gross Annual Salary
gross_annual_salary=(gross_monthly_salary*12)+bonus

#Displaying the enployee details
print(f"Enmployee name: {name}")
print(f"Enmployee id: {id}")
print(f"Enmployee Gross monthly Salary: ₹{gross_monthly_salary:,.2f}")
print(f"Enmployee Gross Annual Salary: ₹{gross_annual_salary:,.2f}")