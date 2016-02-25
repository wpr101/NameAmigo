import random

from util import ReadText as rt

def create_business_name():
    print("Choose the business type:")
    print("Coffee")
    business_type = input()

    if (business_type == "Coffee"):
        words = rt.read_text('../txt/coffeeWords.txt')
        for i in range(100):
            project_name = random.choice(words) + random.choice(words)
            print (project_name)

