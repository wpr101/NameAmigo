def read_text(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    f.close()
    return lines

#Better to have a dictionary than double return?
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

#TESTING 
#prefixWords, meanings = readTextWithMeanings('../txt/readingRocketsPrefix.txt')
#print(prefixWords)
#print(meanings)

