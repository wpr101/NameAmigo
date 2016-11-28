import nltk
from nltk.corpus import gutenberg

blake = nltk.corpus.gutenberg.words('blake-poems.txt')
blake_sentences = gutenberg.sents('blake-poems.txt')


#for i in range(len(blake_sentences)):
    #print(blake_sentences[i])

sentence = ""
for i in range(5,10):
    for j in blake_sentences[i]:
        sentence += j + " " 

print(sentence)
