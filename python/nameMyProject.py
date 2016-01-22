import oneWordProjects
import twoWordProjects

print("Choose an option")
print("1) One Word Project Names")
print("2) Two Word Project Names")

choice = int(input())
if (choice == 1):
    oneWordProjects.createNamesWithMeanings()
elif (choice == 2):
    twoWordProjects.createNames()
