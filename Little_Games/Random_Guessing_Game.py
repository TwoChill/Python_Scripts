from random import randint
secret = randint(1,10)

print("The Guessing Game\n")

quess = 0
while secret != quess:
    g = input("Guess a number!: ")
    guess = int(g)
#   if guess == 0:
#       break
    elif guess == secret:
        print("You won!\n")
        break
    else:
        if guess < secret:
            print("To low!")
        else:
            print("To high!")

print("Game Over!!")
