import random

count = 0

numberrandom1 = random.randint(1, 100)
numberrandom2 = random.randint(1, 100)

number1 = int(numberrandom1)
number2 = int(numberrandom2)

numers = number1 + number2
print('Let\'s play a Game!')
print(f'What is {numberrandom1} + {numberrandom2}')

answer = int(input('Answer: '))

if answer == numers:
    print('You did it good!')
else:
    print('Oops you lose.')
