import random
number = random.randint(1, 10)
tries = 1

uname = input('What is your username?')
print('Hello', uname + '!!!')

question = input('Would you like to play a game? [Y/N]')
if question =='N':
    print('Oh...okay')

if question == 'Y':
    print('Im thinking of a number between 1 & 10')
    guess = int(input('Have a guess:'))


    if guess > number:
        print('Guess lower!!!')
    if guess < number:
        print('Guess higher!!!')

    while guess != number:
        tries +=1
        guess = int(input("try again"))
    if guess < number:
        print('Guess higher!!!')

    if guess == number:
        print('You are right!!!  You win!!!')