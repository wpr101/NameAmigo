import random
import os

def createNames():
    words = readText('words.txt')
    projectNames = []
    for i in range(10):
        projectName = random.choice(words) + random.choice(words)
        projectNames.append(projectName)
    return(projectNames)

def readText(fileName):
    with open(fileName) as f:
        lines = f.read().splitlines()
    f.close()
    return lines









