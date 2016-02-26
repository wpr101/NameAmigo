import random

NUM_NAMES = 1000

def create_names():
    prefix = read_text('prefix.txt')
    suffix = read_text('suffix.txt')
    for i in range(NUM_NAMES):
        name = random.choice(prefix) + random.choice(suffix)
        print(name)

def create_names_with_meanings():
    project_names = []
    prefixes, pre_meanings = read_text_with_meanings('readingRocketsPrefix.txt')
    suffixes, suf_meanings = read_text_with_meanings('readingRocketsSuffix.txt')
    for i in range(NUM_NAMES-1):
        choice_pre = random.randint(0, len(prefixes)-1)
        prefix = prefixes[choice_pre]
        pre_meaning = pre_meanings[choice_pre]

        choice_suf = random.randint(0, len(suffixes)-1)
        suffix = suffixes[choice_suf]
        suf_meaning = suf_meanings[choice_suf]

        name = prefix + suffix
        meaning = pre_meaning + ' ' + suf_meaning
        project_names.append(name)
    return(project_names)

def read_text(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    f.close()
    return lines

def read_text_with_meanings(file_name):
    prefix_words = []
    meanings = []
    with open(file_name) as f:
        lines = f.read().splitlines()
    f.close()
    for i in range(len(lines)):
        word, mean = lines[i].split()
        prefix_words.append(word)
        meanings.append(mean) 
    return prefix_words, meanings




