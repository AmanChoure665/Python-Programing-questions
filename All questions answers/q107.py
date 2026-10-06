"""
Q107. Reverse Word Order

Take a sentence as input. Reverse the order of words (not the characters in
each word). Example: "Python is fun" -> "fun is Python".
"""

def reverse_sentence(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

sentence = "Python is fun"
print(reverse_sentence(sentence))