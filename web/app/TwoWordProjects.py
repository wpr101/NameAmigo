import random
import os

def create_names():
    words = read_text('words.txt')
    project_names = []
    for i in range(1000):
        project_name = random.choice(words) + random.choice(words)
        project_names.append(project_name)
    return(project_names)

def read_text(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    f.close()
    return lines









