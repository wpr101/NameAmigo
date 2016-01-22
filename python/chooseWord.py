import random
import ReadText as rt
from random import randint

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



def createThesaurusName():
    print('Type word from list which describes your project:')
    print('Strong')
    print('Fast')
    userWord = input()
    
    words = rt.readText('../txt/words.txt')
    for i in range(100):
        projectName = ""
        genericWord = random.choice(words)
        thesaurusWord = random.choice(t[userWord])
        order = randint(0,1)
        if order == 0:
            projectName = genericWord + thesaurusWord
        elif order == 1:
            projectName = thesaurusWord + genericWord
        print(projectName)


