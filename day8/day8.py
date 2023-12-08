import math
import time

def num_steps(curr_key, letter_map, final_key=None):
    steps = 0
    curr_key = curr_key
    final_key = final_key
    letter_map = letter_map
    destination_reached = False
    while destination_reached == False:
        for i in instructions:
            steps += 1
            if i == 'L':
                curr_key = letter_map[curr_key][0]
            else:
                curr_key = letter_map[curr_key][1]
            if final_key is None:
                if curr_key.endswith('Z'):
                    destination_reached = True
                    break
            else:
                if curr_key == final_key:
                    destination_reached = True
                    break
    return steps

def lcm_of_list(numbers):
    def lcm(x, y):
        return x * y // math.gcd(x, y)
    result = 1
    for number in numbers:
        result = lcm(result, number)
    return result

start_time_1 = time.time()
letter_map = {}
with open('day8.txt', 'r') as file:
    for i, line in enumerate(file):
        if i == 0:
            instructions = [x for x in line.strip()]
        elif i == 1:
            continue
        else:
            key, vals = line.split('=')
            key = key.strip()
            # if i == 2:
            #     curr_key = key
            L_val, R_val = vals.split(',')
            L_val = L_val.replace('(', '').strip()
            R_val = R_val.replace(')', '').strip()
            letter_map[key] = (L_val, R_val)

part1_ans = num_steps('AAA', letter_map, 'ZZZ')
end_time_1 = time.time()

curr_keys = [key for key in letter_map.keys() if key.endswith('A')]
steps_for_key = []
for curr_key in curr_keys:
    steps_for_key.append(num_steps(curr_key, letter_map, final_key=None))
part2_ans = lcm_of_list(steps_for_key)
end_time_2 = time.time()

part1_time = round((end_time_1-start_time_1) * 1000, 2)
part2_time = round((end_time_2-end_time_1) * 1000, 2)
print(f'Part 1: {part1_ans} ({part1_time} ms), Part 2: {part2_ans} ({part2_time} ms)')
