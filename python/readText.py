def readText(fileName):
    with open(fileName) as f:
        lines = f.read().splitlines()
    f.close()
    return lines

#Better to have a dictionary than double return?
def readTextWithMeanings(fileName):
    prefixWords = []
    meanings = []
    with open(fileName) as f:
        lines = f.read().splitlines()
    f.close()
    for i in range(len(lines)):
        word, mean = lines[i].split()
        prefixWords.append(word)
        meanings.append(mean) 
    return prefixWords, meanings

#TESTING 
#prefixWords, meanings = readTextWithMeanings('../txt/readingRocketsPrefix.txt')
#print(prefixWords)
#print(meanings)

