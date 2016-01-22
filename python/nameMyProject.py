import oneWordProjects
import twoWordProjects
import chooseWord

print("Choose an option")
print("1) One Word Project Names")
print("2) Two Word Project Names")
print("3) Choose Word Describing Project")

choice = int(input())
if (choice == 1):
    oneWordProjects.createNamesWithMeanings()
elif (choice == 2):
    twoWordProjects.createNames()
elif (choice == 3):
    chooseWord.createThesaurusName()
