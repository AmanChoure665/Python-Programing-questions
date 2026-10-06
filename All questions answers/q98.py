"""
Q98. Clean Phone Number

Take a phone number as input in the format +91-98765-43210. Remove all dashes
and the country code. Print the cleaned 10-digit number.
"""

            
def clean_no(ph_no:str):
    ph_no = ph_no.replace("-","")
    ph_no = "".join(ph_no)
    return f"Cleaned phone number: {ph_no[3::]}"


ph_no = input('''Enter your indian phone number in this format - 
                +91-98765-43210 : ''')

print(clean_no(ph_no))