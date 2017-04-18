from random import randrange

answer = randrange(1, 10)
value = 0

#check if guess is a number, then check if it is between 1-10.
#Break the loop and move on once 1-10 number is given.
while True:
    try:
        guess = int(input ("I am thinking of a number from 1-10.  Take a guess.\n"))
    except ValueError:
        print ("That does not look like a number. Guess again.\n")
        continue
    if guess < 1 or guess > 10:
        print ("Please guess a number from 1-10")
    else:
        break

#The game. value is the guess number.
while guess != answer:
    if guess > answer:
        value += 1
        try:
            guess = int(input ("Lower. That was guess number " + str(value) + ". Guess again.\n"))
        except ValueError:
            print ("That does not look like a number. Guess again.\n")
        if guess < 1 or guess > 10:
            print ("Please guess a number from 1-10\n")
    elif guess < answer:
        value += 1
        try:
            guess = int(input ("Higher. That was guess number " + str(value) + ". Guess again.\n"))
        except ValueError:
            print ("That does not look like a number. Guess again.\n")
        if guess < 1 or guess > 10:
            print ("Please guess a number from 1-10\n")
    else:
        break

#add the correct guess to the guess number.    
value += 1
print ("Correct! " + str(guess) + " was my number. It took you " + str(value) + " tries.")
        


#  cd Desktop/Python

