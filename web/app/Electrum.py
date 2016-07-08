import random

import ReadText as rt

NUM_SEEDS = 25

def create_names():
	seeds_list = []
	words = rt.read_text('txt/electrum.txt')

	for i in range(NUM_SEEDS):
		seed_phrase = random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words) + " " + random.choice(words)
		#print("seed_phrase is: ", seed_phrase)
		seeds_list.append(seed_phrase)


	return(seeds_list)

create_names()
