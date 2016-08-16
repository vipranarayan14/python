from random import randint

num = randint(0,9)
running = True


while running:
    guess = int(input('Enter an integer : '))
    print "You entered:" , guess

    if guess == num:
        print("Your guess is correct")
        running = False

    elif guess < num:
        print("No, it is a little higher than that!")

    else:
        print("No, it is a little lower than that")

else:
    print("You have won the Game")

print("{0:_^50}".format("Done"))
