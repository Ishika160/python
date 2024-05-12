def calculate_bill_amount(quantity, value_per_item, discount_percentage, tax_percentage):
    total_cost_before_discount = quantity * value_per_item
    discount_amount = (discount_percentage / 100) * total_cost_before_discount
    total_cost_after_discount = total_cost_before_discount - discount_amount
    tax_amount = (tax_percentage / 100) * total_cost_after_discount
    bill_amount = total_cost_after_discount + tax_amount
    
    return bill_amount

# Example usage:
quantity = int(input("Enter the quantity of the item: "))
value_per_item = float(input("Enter the value of the item per unit: "))
discount_percentage = float(input("Enter the discount percentage: "))
tax_percentage = float(input("Enter the tax percentage: "))

# Calculate the bill amount
bill_amount = calculate_bill_amount(quantity, value_per_item, discount_percentage, tax_percentage)

print("The bill amount is:", bill_amount)
