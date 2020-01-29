import random
n = random.randint(1, 5)
guess = int(input("Enter an integer from 1 to 5: "))
while n != "guess":
    print 
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 5: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 5: "))
    else:
        print ("you guessed it!")
        break

    print

***
sample input:
enter the integer from 1 to 5:4
sample output:
you guessed it!
sample input:
enter the integer from 1 to 5:2
sample output:
guess is low
sample input:
enter the integer from 1 to 5:5
sample output:
guess is high

***


