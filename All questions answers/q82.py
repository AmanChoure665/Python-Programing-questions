'''World Capitals
Create a dictionary mapping five countries to their capital cities. Iterate through this
dictionary using the Items() method and print each pair in the format: Country →
Capital.'''


capitals = {
    "India": "Delhi", 
    "Australia": "sydeny", 
    "USA": "Washington DC", 
    "Japan": "Tokyo", 
    "South Korea": "Seol"
}

for country, capital in capitals.items():
    print(f"{country} --> {capital}")