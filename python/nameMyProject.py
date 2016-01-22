import OneWordProjects
import TwoWordProjects
import ChooseWord

def nameMyProject():
    print("Choose an option")
    print("1) One Word Project Names")
    print("2) Two Word Project Names")
    print("3) Choose Word Describing Project")

    choice = int(input())
    if (choice == 1):
        OneWordProjects.createNamesWithMeanings()
    elif (choice == 2):
        TwoWordProjects.createNames()
    elif (choice == 3):
        ChooseWord.createThesaurusName()

while(True):
    nameMyProject()
