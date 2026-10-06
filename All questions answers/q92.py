'''
    Using a for loop, check if there is any vovels
'''

text = "programming"
total = 0
n = len(text)
i = 0
while i < n:
    if text[i] == "m" or text[i] == "M":
            total += 1
    i += 1
        
print(f"Total {total} no. of 'm' in the text.")