import random


winning_numbers = []
player_numbers = input('Welcome to the lottery 6/49.\nPlease in input your six numbers separated by coma and press enter.\n').split(',')
player_list = list(map(int, player_numbers))
winners = []

# creating the winning numbers.
for i in range(0, 6):
    number = random.randint(1, 49)
    winning_numbers.append(number)
print('The wining numbers are:')
print(*winning_numbers, sep=", ")


# creating a list with the matching numbers.
for num in winning_numbers:
    if num in player_list:
        winners.append(num)


# finding if We win and how much is the winning price.
if 0 < len(winners) <= 2:
    print(f'You guessed only {len(winners)}\nHave a good day!')
elif len(winners) > 2:
    if len(winners) == 3:
        print(f"You guessed 3 numbers. You won $5!")
    elif len(winners) == 4:
        print(f"You guessed 4 numbers. You won $30!")
    elif len(winners) == 5:
        print(f"You guessed 5 numbers. You won $100!")
    else:
        print(f'You got the jackpot! $500 :)')
else:
    print(f"You didn't guess any number.\nHave a good day!")
