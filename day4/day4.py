sum1 = 0
sum2 = 0
card_multipliers = {key: 1 for key in range(1, 199)}

with open('day4.txt', 'r') as file:
    for i, line in enumerate(file):
        card_points = 0
        num_cards_won = 0
        card_multiplier = card_multipliers.get(i+1)
        card = line.split(':')
        card_num = int(''.join(char for char in card[0] if char.isdigit()))
        numbers = card[1].split('|')
        winning_numbers = [int(digit) for digit in numbers[0].strip().split()]
        my_numbers = [int(digit) for digit in numbers[1].strip().split()]
        for num in my_numbers:
            if num in winning_numbers:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points = card_points * 2
                num_cards_won += 1
        card_nums_won = [card_num + i for i in range(1, num_cards_won + 1)]
        for i in card_nums_won:
            card_multipliers[i] += 1 * card_multiplier
        sum1 += card_points

sum2 = sum(card_multipliers.values())

print(f'Part 1: {sum1}, Part 2: {sum2}')
