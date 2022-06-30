import random 

print ("Number Guessing Game")

number = random.randint(1,9)
chances = 0

print ("Guess The Value Between 1 To 9: ")
while chances < 5:
    guess = int(input("Enter Your Guess: "))
    if guess == number:
        print ("Congratulations You Won")
        break 
    elif guess < number:
        print ("Guess Is Too Low Guess A Number Higher Than ",guess)

    else :
        print ("Your Guess Was Too High Guess A Number Lower Than ",guess)

    chances+=1

if not chances < 5 :
    print ("You Loose The Number Is ",number)