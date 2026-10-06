'''
check if there is any vovels
'''

text = "programming"

total = 0
for ch in text:
    if ch in "aeiouAEIOU":
        total += 1
        
print(total)