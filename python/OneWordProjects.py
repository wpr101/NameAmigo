import random
from util import ReadText as rt

NUM_NAMES = 100

def createNames():
    prefix = rt.readText('../txt/prefix.txt')
    suffix = rt.readText('../txt/suffix.txt')
    for i in range(NUM_NAMES):
        name = random.choice(prefix) + random.choice(suffix)
        print(name)

def createNamesWithMeanings():
    prefixes, preMeanings = rt.readTextWithMeanings('../txt/readingRocketsPrefix.txt')
    suffixes, sufMeanings = rt.readTextWithMeanings('../txt/readingRocketsSuffix.txt')
    for i in range(NUM_NAMES):
        choicePre = random.randint(0, len(prefixes)-1)
        prefix = prefixes[choicePre]
        preMeaning = preMeanings[choicePre]

        choiceSuf = random.randint(0, len(suffixes)-1)
        suffix = suffixes[choiceSuf]
        sufMeaning = sufMeanings[choiceSuf]

        name = prefix + suffix
        meaning = preMeaning + ' ' + sufMeaning
        #print(name + ' means: ' + meaning)
        print(name)


