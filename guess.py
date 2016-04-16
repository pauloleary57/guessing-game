'''
Created on Mar 20, 2016

@author: Paul
'''
from random import randint

def main():
    print "Welcome to the number guessing game! You will have 5 chances to guess."
    num = randint(1, 10)
    guesses = 0
    print "I have my number..."
    while True:
        guess = raw_input("What is your guess [1 - 10]? ")
        guesses += 1
        if int(guess) == num:
            print "You got it! Thanks for playing!"
            break
        elif guesses == 5:
            print "That's not correct and that's 5 guesses. The number was " + str(num) + "."
            break
        else:
            print "Not correct, please try again."            
                
if __name__ == '__main__':
    main()