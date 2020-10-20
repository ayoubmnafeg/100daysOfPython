
from random import randint

c = True
while c:
    num = input('Maximum number you wanna guess: ')
    if num.isdigit():
        print('\tlet''s go!!')
        num = int(num)
        c = False
    else:
        print('try again')

r = randint(1, num)
guess = None
count = 1

while guess != r:
    guess = input('guess the number:')
    if guess.isdigit():
        guess = int(guess)
    if guess > r:
        print('\tToo higt!')
        count += 1
    elif guess < r:
        print('\tToo low!')
        count += 1

if count == 1:
    print('\tYou are a SuperHero !!!!')
else:
    print('\tYou win after ' + str(count) +' guesses!')