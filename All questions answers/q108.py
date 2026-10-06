"""
Q108. PAN Card Validation

Take a string as input. Check if it is a valid Indian PAN card number. Format: 5
uppercase lettere & 1 dinite + 1 unnerrace latter (Total 10 charactere) Example:
ABCDE1234F.
"""

pan_no = "CWKPC2900H"

if (len(pan_no) == 10
    and pan_no[0:5].isalpha() 
    and pan_no[0:5].isupper()
    and pan_no[-1].isalpha()
    and pan_no[-1].isupper()
    and pan_no[5:9].isdigit()):
    
    print("Valid")
else:
    print("Invalid")