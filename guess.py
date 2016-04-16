'''
Created on Mar 20, 2016

@author: Paul
'''
from random import randint

def main():
    print "Welcome to the number guessing game!"
    num = randint(1, 10)
    print "I have my number..."
    while True:
        guess = raw_input("What is your guess [1 - 10]? ")
        if int(guess) == num:
            break
        else:
            if int(guess) < num:
                print "That's too low, try again!"
            else:
                print "That's too high, try again!"
    print "You got it! Thanks for playing!"            
                
if __name__ == '__main__':
    main()