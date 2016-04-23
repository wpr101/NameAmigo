import random

VOWELS = ("A", "E", "I", "O", "U")
CONSONANTS = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q",
              "R", "S", "T", "V", "W", "X", "Y", "Z")
ENTRIES = 100

def pattern_cvcv():
    letter_one = random.choice(CONSONANTS)
    letter_two = random.choice(VOWELS)
    letter_three = random.choice(CONSONANTS)
    letter_four = random.choice(VOWELS)
    name = letter_one + letter_two.lower() + letter_three.lower() + letter_four.lower()
    return(name)

def generate_patterns():
    name_list = []
    for i in range(ENTRIES):
        name_list.append(pattern_cvcv())
    return(name_list)



