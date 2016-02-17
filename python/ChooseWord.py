import random
from random import randint

from util import ReadText as rt


t = {}
t.update({'Strong':['Strong', 'Able', 'Active', 'Big',
                    'Energy', 'Firm',
                    'Force', 'Heavy', 'Robust', 'Secure',
                    'Solid', 'Stable', 'Steady',
                    'Tough', 'Vigor', 'Might',
                    'Rugged', 'Sound']})

t.update({'Fast':['Fast', 'Agile', 'Brisk', 'Hot', 'Quick',
                  'Rapid', 'Swift', 'Accel', 'Active',
                  'Dash', 'Flash', 'Fly', 'Race', 'Snap',
                  'Wing', 'Streak', 'Time', 'Chop', 'Jiffy',
                  'Split', 'Bat', 'Crazy', 'Double', 'Scream',
                  'Sonic', 'Super', 'Ball', 'Speed']})

def create_thesaurus_name():
    print('Type word from list which describes your project:')
    print('Strong')
    print('Fast')
    user_word = input()
    
    words = rt.read_text('../txt/words.txt')
    for i in range(100):
        project_name = ""
        generic_word = random.choice(words)
        thesaurus_word = random.choice(t[user_word])
        order = randint(0,1)
        if order == 0:
            project_name = generic_word + thesaurus_word
        elif order == 1:
            project_name = thesaurus_word + generic_word
        print(project_name)


