import random
from random import randint

import ReadText as rt

def custom_names(user_word):
    words = rt.read_text('txt/words.txt')
    project_names = []
    for i in range(25):
        order = randint(0,1)
        select_num = randint(0,len(user_word)-1)
        select_word = user_word[select_num]
        if order == 0:
            project_name = select_word + random.choice(words)
        elif order == 1:
            project_name = random.choice(words) + select_word
        project_names.append(project_name)
    return(project_names)
