import OneWordProjects
import TwoWordProjects
import ChooseWord
import BusinessType

def name_my_project():
    print("")
    print("Choose an option")
    print("1) One Word Project")
    print("2) Two Word Project")
    print("3) Word Describing Project")
    print("4) Business Type")

    choice = int(input())
    if (choice == 1):
        OneWordProjects.create_names_with_meanings()
    elif (choice == 2):
        TwoWordProjects.create_names()
    elif (choice == 3):
        ChooseWord.create_thesaurus_name()
    elif (choice == 4):
        BusinessType.create_business_name()

while(True):
    name_my_project()
