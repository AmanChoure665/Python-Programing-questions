"""
Q106. Word Lengths (Homework)

Take a sentence as input. Print each word's length next to it.
Example: Python (6) is (2) great (5).
"""



def word_length(sentence):
    words = sentence.split()
    my_lst = []
    for word in words:
        n = len(word)
        my_lst.append(f"{word} ({n})")
    return " ".join(my_lst)

sentence = "Anirudh is learning Python programming every single day"
print(word_length(sentence))
