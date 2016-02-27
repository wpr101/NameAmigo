import random
import os

import ReadText as rt

def create_names():
    words = rt.read_text('txt/words.txt')
    project_names = []
    for i in range(25):
        project_name = random.choice(words) + random.choice(words)
        project_names.append(project_name)
    return(project_names)










