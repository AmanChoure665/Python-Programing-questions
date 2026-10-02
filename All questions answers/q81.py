''' Product Price Lookup
Construct a dictionary containing four product names and their prices. Prompt
the user to enter a product name. Use the in keyword to check if it exists; if
so, display its price. Otherwise, inform the user "Product not found."'''


products = {
    "cable": 99, 
    "connector": 100, 
    "keyboard": 988, 
    "powerbank": 743, 
    "mouse": 671
}

prompt = input("Enter a product name: ")

if prompt in products:
    print(f"Price of {prompt} = {products.get(prompt)}")
else:
    print("Product not found")