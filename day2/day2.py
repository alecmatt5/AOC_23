import re
red = 12
green = 13
blue = 14

red_pattern = r'(\d+)\s+red'
green_pattern = r'(\d+)\s+green'
blue_pattern = r'(\d+)\s+blue'

sum1 = 0
sum2 = 0
# file = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
#             'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
#             'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
#             'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
#             'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
with open('day2.txt', 'r') as file:
    for line in file:
        possible = True
        game_id = line.split(':')
        games = game_id[1]
        game_id = ''.join(filter(str.isdigit, game_id[0]))
        red_matches = re.findall(red_pattern, line)
        max_red = 0
        for i in red_matches:
            if int(i) > max_red:
                max_red = int(i)
            if int(i) > red:
                possible = False
        green_matches = re.findall(green_pattern, line)
        max_green = 0
        for i in green_matches:
            if int(i) > max_green:
                max_green = int(i)
            if int(i) > green:
                possible = False
        blue_matches = re.findall(blue_pattern, line)
        max_blue = 0
        for i in blue_matches:
            if int(i) > max_blue:
                max_blue = int(i)
            if int(i) > blue:
                possible = False
        if max_red == 0:
            max_red = 1
        if max_green == 0:
            max_green = 1
        if max_blue == 0:
            max_blue = 1
        round_power = max_red * max_green * max_blue
        sum2 += round_power
        if possible == True:
            sum1 += int(game_id)
print(sum1)
print(sum2)
