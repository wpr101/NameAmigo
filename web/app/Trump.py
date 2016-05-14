import random

import ReadText as rt

NUM_NAMES = 25

def create_names():
	name_list = []
	first_names = rt.read_text('txt/first_names.txt')
	last_names = rt.read_text('txt/last_names.txt')

	for i in range(NUM_NAMES):
		name = random.choice(first_names) + " " + random.choice(last_names)
		print("name is: ", name)
		name_list.append(name)


	return(name_list)
