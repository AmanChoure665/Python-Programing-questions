"""
Q99. Vowel-Starting Words

Take a sentence as input. Split it into words and print how many words start
with a vowel.
"""



def check_vowel(sentence):
    sentence = sentence.split()
    count = 0
    for word in sentence:
        if word[0] in "aeiouAEIOU":
            count += 1

    return f" Total words starts with vowel = {count}"


sentence = "aman is a good coder and is learning python"

print(check_vowel(sentence))