import random


def checking_result(number, guess, current_money):
    player_number_list = guess.split()
    if len(player_number_list) > current_money:
        print(f'Not enough money for this bet. You have {current_money}')
        return current_money
    current_money -= len(player_number_list)
    for el in range(len(player_number_list)):
        if player_number_list[el] == '>18' and number > 18:
            print('You won $2')
            current_money += 2
        if player_number_list[el] == '<19' and number < 19:
            print('You won $2')
            current_money += 2
        if player_number_list[el].isdigit() and number == int(player_number_list[el]):
            print('You won $36')
            current_money += 36
        if player_number_list[el] == 'odd' and number % 2 != 0:
            print('You won $2')
            current_money += 2
        if player_number_list[el] == 'even' and number % 2 == 0:
            print('You won $2')
            current_money += 2
    print(f'Your current money are: ${current_money}')
    return current_money


# creating the roulette numbers.
american_roulette_numbers = [00]
for i in range(37):
    american_roulette_numbers.append(i)

# starting the game.
print('Welcome to the roulette game!\nYou are starting with $100 and each bet is $1!\nThe game finish when you enter "End"!')
print()
player_bet = input('Please place your bet and press enter.\nYou can choose to bet on numbers, odd, even, >18 or <19.\nIf you choose multiple bets, please separate it with space: ')


# finding the result.
player_money = 100
while player_bet != 'End':
    winning_number = random.choice(american_roulette_numbers)
    print(f'The wining number is: {winning_number}')
    print()
    player_money = checking_result(winning_number, player_bet, player_money)
    if player_money == 0:
        print(f'No more money! Game over!')
        break
    player_bet = input('Please choose your next bet: ')

