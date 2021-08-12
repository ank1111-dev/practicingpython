import random

num = random.randint(1, 99)
guess= None


while guess != num:

    guess = input("Guess a number between 1 and 99:")
    guess = int(guess)
    
     
    if guess == num:
        print("Hurray!!Your guess is correct.")
        break
    else:
        print("Sorry, your guess is wrong.Try again")


        

            
