# import module to generate random number
import random

# setting the range of numbers
min_value=1
max_value=6

# to loop the rolling through user input
roll_the_dice="yes"


while roll_the_dice=="yes" or roll_the_dice=="y":
    print("Rolling the dices")
    print("The values are:")
    # Generating and Printing the number on first dice
    print(random.randint(min_value,max_value))
    # Generating and Printing the number on second dice
    print(random.randint(min_value,max_value))

    #Asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_the_dice=input("Do you want to roll the dices again?")

