import string

def clean_words(user_word):
    #remove punctuation
    punct = set(string.punctuation)
    user_word = ''.join(x for x in user_word if x not in punct)

    #split words on spaces
    word_list = user_word.split()
    for i in range(len(word_list)):
        word_list[i] = word_list[i].capitalize()
		
    #remove duplicates from the list
    word_list = list(set(word_list))

    #remove stop words from the text
    stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']
    for s in stop:
        for w in word_list:
            if (s.capitalize() == w):
                word_list.remove(w)

    return (word_list)

def create_redirect_string(word_list):	
    redirect_string = '/custom-words/'
    for i in range(len(word_list)):
        redirect_string += word_list[i] 
        redirect_string += "-"
    #remove the trailing slash
    redirect_string = redirect_string[:-1]
    return(redirect_string)
    
