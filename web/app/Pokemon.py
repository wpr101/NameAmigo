import random

import ReadText as rt

NUM_SEEDS = 25

def create_names():
	seeds_list = []
	words = rt.read_text('txt/pokemon.txt')

	for i in range(NUM_SEEDS):
		seed_phrase = random.choice(words)
		seeds_list.append(seed_phrase)


	return(seeds_list)

#create_names()
