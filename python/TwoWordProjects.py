import random
from util import ReadText as rt

def create_names():
    words = rt.read_text('../txt/words.txt')
    for i in range(100):
        project_name = random.choice(words) + random.choice(words)
        print (project_name)











