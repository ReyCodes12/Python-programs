#Project Income Tax Calculator Reynol Garcia 03/19/2023

flatRate = float(0.20)
standard_Deduction = 10000
dependent_Deduction = 3000

grossIncome = float(input("Enter the gross income: "))

dependent = int(input("Enter the number of dependents: ")) * dependent_Deduction

income_Tax = (grossIncome - standard_Deduction - dependent_Deduction) * flatRate

print("The income tax is $", income_Tax)