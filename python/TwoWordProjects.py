import random
from util import ReadText as rt

def createNames():
    words = rt.readText('../txt/words.txt')
    for i in range(100):
        projectName = random.choice(words) + random.choice(words)
        print (projectName)











