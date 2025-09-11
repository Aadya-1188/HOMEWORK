def calculate_due(total_bill, amount_paid):
    due_amount = total_bill - amount_paid
    return due_amount

# Get input from the user
total_bill = float(input("Enter the total bill amount: ₹"))
amount_paid = float(input("Enter the amount paid by the customer: ₹"))

# Call the function and store the result
due = calculate_due(total_bill, amount_paid)

# Show the result
if due > 0:
    print(f"The customer still owes ${due:.2f} ")
elif due == 0:
    print("The bill is fully paid!")
else:
    print(f"The customer overpaid by ${abs(due):.2f} ")
