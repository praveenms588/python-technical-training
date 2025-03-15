annual_income=float(input("Enter annual income: "))
standard_deductions=50000

#Calculate taxable income
taxable_income=annual_income-standard_deductions

#Display 
print(f"Annual income: ₹{annual_income:,.2f}")
print(f"Standard Deductions: ₹{standard_deductions:,.2f}")
print(f"Taxable Income: ₹{taxable_income:,.2f}")