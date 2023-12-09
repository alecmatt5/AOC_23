import time
import numpy as np

inputs = []
with open('day9.txt', 'r') as file:
    for line in file:
        inputs.append(list(map(int, line.split())))

def predict_next_value(sequence, reverse=False):
    if reverse == True:
        sequence = sequence[::-1]
    sum = 0
    last_val = sequence[-1]
    while len(sequence) > 1:
        differences = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
        sum += differences[-1]
        if all(diff == 0 for diff in differences):
            return sum + last_val
        else:
            sequence = differences

start_time_1 = time.time()
part1_ans = 0
for sequence in inputs:
    part1_ans += predict_next_value(sequence)
end_time_1 = time.time()

part2_ans = 0
for sequence in inputs:
    part2_ans += predict_next_value(sequence, reverse=True)
end_time_2 = time.time()

part1_time = round((end_time_1-start_time_1) * 1000, 2)
part2_time = round((end_time_2-end_time_1) * 1000, 2)
print(f'Part 1: {part1_ans} ({part1_time} ms), Part 2: {part2_ans} ({part2_time} ms)')
