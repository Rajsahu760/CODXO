# CODXO
import random
ans=random.randrange(1,101)
chance=0

while chance < 10:
    guess=int(input("Guess the number between 1 to 100= "))

    if guess == ans:
        print("You won the game !")
    if guess < ans :
        print("Choose higher value!")
    if guess > ans :
        print("Choose lower value!")
    
    chance=chance+1

    if chance == 10:
        print("GAME OVER!!")
        print("##########")
        print("The answer was:",ans)
