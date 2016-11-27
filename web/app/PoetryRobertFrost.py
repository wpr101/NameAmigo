import random

import ReadText as rt

NUM_SEEDS = 12
BLANK_SPACE_SEP = 4

def create_names():
    seeds_list = []
    words = rt.read_text('txt/poetry_robert_frost.txt')

    for i in range(NUM_SEEDS):
        seed_phrase = random.choice(words)
        #insert a blank space randomly
        rand_int = random.randint(1,BLANK_SPACE_SEP)
        if (rand_int == 1):
            seeds_list.append("")
        seeds_list.append(seed_phrase)

    return(seeds_list)

create_names()
