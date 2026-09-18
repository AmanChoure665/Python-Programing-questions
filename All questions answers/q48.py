"""Write a function tax_calcu;lator(income) that takes annual income 
and returns the tax amount based on these slabs:
» Up to 2,50,000 → No tax
» 2,50,001 to 5,00,000 → 5%
» 5,00,001 to 10,00,000 → 20%
» Above 10,00,000 → 30%
"""

def tax_calculator(income):
    if income <= 250000:
        return "No tax"
    elif income <= 500000:
        return f"Tax is 5% of your income {income * 0.05}"
    elif income <= 1000000:
        return f"Tax is 20% of your income {income * 0.20}"
    else:
        return f"Tax is 30% of your income {income * 0.30}"

print(tax_calculator(5825241))
print(tax_calculator(582524))
print(tax_calculator(150000))
print(tax_calculator(300000))