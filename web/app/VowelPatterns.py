import random

VOWELS = ("a", "e", "i", "o", "u")
CONSONANTS = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q",
              "r", "s", "t", "v", "w", "x", "y", "z")
ENTRIES = 100

def pattern_cvcv():
    letter_one = random.choice(CONSONANTS).upper()
    letter_two = random.choice(VOWELS)
    letter_three = random.choice(CONSONANTS)
    letter_four = random.choice(VOWELS)
    name = letter_one + letter_two + letter_three + letter_four
    return(name)

def generate_patterns():
    name_list = []
    for i in range(ENTRIES):
        name_list.append(pattern_cvcv())
    return(name_list)

