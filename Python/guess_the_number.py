import random

num = random.randint(1,20)
user_num = int(input("Guess a number between (and including) 1 and 20: "))
correct_guess = False

#Func for determinging if user input meets constraints
def isValidInput(usernum):
    if usernum < 1 or usernum > 20:
        return False
    return True

#Func for number direction
def direction ():
    if user_num > num:
        return "Your guess is too high!"
    else:
        return "Your guess is too low!"

while not correct_guess:
    while not isValidInput(user_num):
        user_num = int(input("Invalid input. Please enter a number between 1 and 20 "))
        isValidInput(user_num)
    if user_num == num:
        print("You Guessed right! %d is the correct number" % (num))
        correct_guess = True
    else:
        print("You Guessed wrong! %s Try again!" % (direction()))
        user_num = int(input("Guess a number between (and including) 1 and 20: "))
