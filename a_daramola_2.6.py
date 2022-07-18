#Akinola Daramola Jr
#Programming Exerccise 2.6
#Due Date: 6/16/2020

"""Write a program that will ask the user to enter the amount of a purchase.
#The program should then compute the state and county sales tax.
Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent.
The program should display the amount of the purchase, the state sales tax,
the county sales tax, the total sales tax, and the total of the sale (which is the sum of the amount of purchase plus the total sales tax).
Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent."""

#Declared Variables
amount = 0.0
amount = float(input("Enter the amount of purchase? "))
state_sales_tax = .05
county_sales_tax = .025


#Computing state tax amount
state_tax_amount = amount * state_sales_tax

#Computing county tax amount
county_tax_amount = amount * county_sales_tax

#Computing total tax amount
total_tax_amount = state_tax_amount + county_tax_amount

#Computing total purchase amount
total_purchase_amount = amount + total_tax_amount


#Amount of Purchase
print(f"Amount of purchase: ${amount:.2f}")

#State sales tax
print(f"State sale tax: {state_tax_amount: .2}")

#County sales tax
print(f"County sales tax: {county_tax_amount: .2}")

#Total sales tax
print(f"Total sales tax: {total_tax_amount:.2}")

#Total purchase amount
print(f"Total of sale: ${total_purchase_amount:.2f}")


