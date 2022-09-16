#Greetings
print("Hi there , \"Welcome to the Guess The Number\" game !")
Name = input("Please enter your name to start : ")

# Game
import random
num = random.randint(0,100)
print("Okay" , Name , "you can guess from number 0 to 100")
Guess = input ("Guess the number : ")
Guess = int(Guess)

# Result
if Guess==num :
    print("You win!!")

else :
    print("You lose :((")

print("Good Game ...")