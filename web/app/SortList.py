import ReadText as rt

def sort_list():
    words = rt.read_text('txt/words.txt')
    sorted_words = sorted(words)
    print(sorted_words)

    with open('sorted_words.txt', mode='wt') as myfile:
    	myfile.write('\n'.join(sorted_words))

sort_list()
