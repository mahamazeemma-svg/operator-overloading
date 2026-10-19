import random

class Fruitquiz:

    def __init__(self):

        self.fruits={'apple':'red',
                    'watermelon':'green',
                    'banana':'yellow',
                    'lychee':'white'}

    def quiz(self):
        while(True):
            fruit,colour = random.choice(list(self.fruits.items()))
            print("what is the colour of my fruit",fruit)
            useranswer = input()
            if useranswer.lower()==colour:
                print("correct answer")
            else:
                print("incorrect answer try again")
            option = int(input("enter 0 if you want to play again, if not then enter 1"))

            if(option):
                break

print("welcome to my quiz")
obj = Fruitquiz()
obj.quiz()