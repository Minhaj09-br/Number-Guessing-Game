# number gasing game
import random
import pyjokes

player=int(input("enter your num:(1,10):"))

computer=random.randint(1,10)


if computer==player:
    jokes=pyjokes.get_joke()
    print(jokes)
    print("you win")

else:
    print("you lose")


