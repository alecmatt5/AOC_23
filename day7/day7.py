from collections import Counter
import time

cards_pos = {}
five_oak = []
four_oak = []
full_house = []
three_oak = []
two_pair = []
one_pair = []
high_card = []

five_oak_2 = []
four_oak_2 = []
full_house_2 = []
three_oak_2 = []
two_pair_2 = []
one_pair_2 = []
high_card_2 = []

time_1 = 0
time_2 = 0

card_strength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
card_strength_wilds = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

with open('day7.txt', 'r') as file:
    for i, line in enumerate(file):
        s1 = time.time()

        temp = line.split()
        cards = list(temp[0])
        bid = int(temp[1])
        cards_pos[i] = bid


        # Part 1:
        card_counts = Counter(cards)
        if 5 in card_counts.values():
            five_oak.append([i, cards])
        elif 4 in card_counts.values():
            four_oak.append([i, cards])
        elif 3 in card_counts.values() and 2 in card_counts.values():
            full_house.append([i, cards])
        elif 3 in card_counts.values():
            three_oak.append([i, cards])
        elif list(card_counts.values()).count(2) == 2:
            two_pair.append([i, cards])
        elif list(card_counts.values()).count(2) == 1:
            one_pair.append([i, cards])
        else:
            high_card.append([i, cards])

        e1 = time.time()

        time_1 += e1 - s1

        # Part 2:
        s2 = time.time()
        cards_no_j = [char for char in temp[0] if char != 'J']
        num_of_js = cards.count('J')
        card_counts = Counter(cards_no_j)
        if num_of_js == 5:
            five_oak_2.append([i, cards])
        elif 5 in card_counts.values() or max(card_counts.values()) + num_of_js == 5:
            five_oak_2.append([i, cards])
        elif 4 in card_counts.values() or max(card_counts.values()) + num_of_js == 4:
            four_oak_2.append([i, cards])
        elif 3 in card_counts.values() and 2 in card_counts.values():
            full_house_2.append([i, cards])
        elif max(card_counts.values()) + num_of_js == 3 and min(card_counts.values()) == 2:
            full_house_2.append([i, cards])
        elif max(card_counts.values()) + num_of_js == 3:
            three_oak_2.append([i, cards])
        elif list(card_counts.values()).count(2) == 2:
            two_pair_2.append([i, cards])
        elif num_of_js == 1 or 2 in card_counts.values():
            one_pair_2.append([i, cards])
        else:
            high_card_2.append([i, cards])
        e2 = time.time()
        time_2 += e2 - s2

s1 = time.time()
def card_sort_key(card_list):
    return [card_strength.index(card) for card in card_list[1]]

five_oak_sorted = sorted(five_oak, key=card_sort_key)
four_oak_sorted = sorted(four_oak, key=card_sort_key)
full_house_sorted = sorted(full_house, key=card_sort_key)
three_oak_sorted = sorted(three_oak, key=card_sort_key)
two_pair_sorted = sorted(two_pair, key=card_sort_key)
one_pair_sorted = sorted(one_pair, key=card_sort_key)
high_card_sorted = sorted(high_card, key=card_sort_key)

sorted_cards = []
sorted_cards.extend(five_oak_sorted)
sorted_cards.extend(four_oak_sorted)
sorted_cards.extend(full_house_sorted)
sorted_cards.extend(three_oak_sorted)
sorted_cards.extend(two_pair_sorted)
sorted_cards.extend(one_pair_sorted)
sorted_cards.extend(high_card_sorted)

part1_ans = 0
for i, hand in enumerate(sorted_cards):
    part1_ans += (len(sorted_cards) - i) * cards_pos[hand[0]]

e1 = time.time()

time_1 += e1 - s1

s2 = time.time()
def card_sort_key_2(card_list):
    return [card_strength_wilds.index(card) for card in card_list[1]]

five_oak_sorted_2 = sorted(five_oak_2, key=card_sort_key_2)
four_oak_sorted_2 = sorted(four_oak_2, key=card_sort_key_2)
full_house_sorted_2 = sorted(full_house_2, key=card_sort_key_2)
three_oak_sorted_2 = sorted(three_oak_2, key=card_sort_key_2)
two_pair_sorted_2 = sorted(two_pair_2, key=card_sort_key_2)
one_pair_sorted_2 = sorted(one_pair_2, key=card_sort_key_2)
high_card_sorted_2 = sorted(high_card_2, key=card_sort_key_2)

sorted_cards_2 = []
sorted_cards_2.extend(five_oak_sorted_2)
sorted_cards_2.extend(four_oak_sorted_2)
sorted_cards_2.extend(full_house_sorted_2)
sorted_cards_2.extend(three_oak_sorted_2)
sorted_cards_2.extend(two_pair_sorted_2)
sorted_cards_2.extend(one_pair_sorted_2)
sorted_cards_2.extend(high_card_sorted_2)

part2_ans = 0
for i, hand in enumerate(sorted_cards_2):
    part2_ans += (len(sorted_cards_2) - i) * cards_pos[hand[0]]

e2 = time.time()
time_2 += e2 - s2

part1_time = round(time_1 * 1000, 2)
part2_time = round(time_2 * 1000, 2)

print(f'Part 1: {part1_ans} ({part1_time} ms), Part 2: {part2_ans} ({part2_time} ms)')
