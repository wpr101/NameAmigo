import OneWordProjects
import TwoWordProjects
import ChooseWord

def name_my_project():
    print("")
    print("Choose an option")
    print("1) One Word Project Names")
    print("2) Two Word Project Names")
    print("3) Choose Word Describing Project")

    choice = int(input())
    if (choice == 1):
        OneWordProjects.create_names_with_meanings()
    elif (choice == 2):
        TwoWordProjects.create_names()
    elif (choice == 3):
        ChooseWord.create_thesaurus_name()

while(True):
    name_my_project()
