def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage.

  Returns:
    The final price after applying the discount, or the original price if the
    discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Get user input for the original price and discount percentage.
try:
  original_price = float(input("Enter the original price of the item: "))
  discount_percentage = float(input("Enter the discount percentage: "))

  # Calculate the final price using the calculate_discount function.
  final_price = calculate_discount(original_price, discount_percentage)

  # Print the final price.
  if final_price == original_price:
    print("No discount applied. The original price is:", final_price)
  else:
    print("The final price after applying the discount is:", final_price)

except ValueError:
  print("Invalid input. Please enter valid numbers for the price and discount.")
