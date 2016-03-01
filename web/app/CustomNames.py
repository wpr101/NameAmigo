import random
from random import randint

import ReadText as rt

def custom_names(user_word):
    words = rt.read_text('txt/words.txt')
    project_names = []
    for i in range(25):
        order = randint(0,1)
        if order == 0:
            project_name = user_word + random.choice(words)
        elif order == 1:
            project_name = random.choice(words) + user_word
        project_names.append(project_name)
    return(project_names)
