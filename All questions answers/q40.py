"""
Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.
"""

def discount_price(original_price,discount_percent):
    discount_amount = (discount_percent / 100) * original_price
    final_amount = original_price - discount_amount
    return f"{final_amount} is the final price after discount"

o = int(input("Enter the Original price: "))
p = int(input("Enter the Final price: "))

dp = discount_price(o,p)
print(dp)