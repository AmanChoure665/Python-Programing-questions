"""
Q102. Longest Word

Take a sentence as input. Print the longest word in it.
"""

def long_word(sentence:str):
    words = sentence.split()
    return max(words, key=lambda x: len(x))
    # longest_count = 0
    # longest_word = ""
    # for word in words:
    #     if  len(word) > longest_count:
    #         longest_count = len(word)
    #         longest_word = word
    # return longest_word

sentence = "python is great and python is powerful"
print(long_word(sentence))