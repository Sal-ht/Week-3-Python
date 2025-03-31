# Function to calculate the final price after applying the discount

def calculate_discount(price, discount_percent):
    
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price  # No discount applied

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(price, discount_percent)

if final_price == price:
    print(f"No discount applied. The final price is: {final_price}")
else:
    print(f"The final price after applying the discount is: {final_price}")
