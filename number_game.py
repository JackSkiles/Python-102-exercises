#imports random function to allow random number generating
import random

#creates random variable that picks a number between 0 and 10
rand1 = random.randint(0 , 10)



#creates a for loop that iterates 5 times and asks the user for input up to five times. If the user gets it correct the program breaks and congradualtes you.
for i in range(5):
    guess = input('Please input a guess number between 0 and 10 ')
    guess = int(guess)
    if guess == rand1:
        print('good guess! ')
        break
    elif guess != rand1:
        print('try again ')