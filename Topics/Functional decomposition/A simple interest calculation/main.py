def calculate(amount, interest_rate, time):
    # Calculate interest; interest_rate should be provided as a percentage (e.g., 5 for 5%)
    interest = amount * (interest_rate / 100) * time
    # Calculate total amount; the total amount is the initial amount plus the interest
    total_amount = amount + interest
    return interest, total_amount

def print_result(interest, total_amount):
    # Convert numeric values to strings for printing
    print("The interest is: " + str(interest))
    print("The total amount is: " + str(total_amount))


