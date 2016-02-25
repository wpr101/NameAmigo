import random
from util import ReadText as rt

NUM_NAMES = 100

def createNames():
    prefix = rt.read_text('../txt/prefix.txt')
    suffix = rt.read_text('../txt/suffix.txt')
    for i in range(NUM_NAMES):
        name = random.choice(prefix) + random.choice(suffix)
        print(name)

def create_names_with_meanings():
    prefixes, pre_meanings = rt.read_text_with_meanings('../txt/readingRocketsPrefix.txt')
    suffixes, suf_meanings = rt.read_text_with_meanings('../txt/readingRocketsSuffix.txt')
    for i in range(NUM_NAMES):
        choice_pre = random.randint(0, len(prefixes)-1)
        prefix = prefixes[choice_pre]
        pre_meaning = pre_meanings[choice_pre]

        choice_suf = random.randint(0, len(suffixes)-1)
        suffix = suffixes[choice_suf]
        suf_meaning = suf_meanings[choice_suf]

        name = prefix + suffix
        meaning = pre_meaning + ' ' + suf_meaning
        #print(name + ' means: ' + meaning)
        print(name)


