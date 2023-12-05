import re
import time

start_time_1 = time.time()

with open('day5.txt', 'r') as file:
    text = file.read()

# Split the text based on empty lines
sections = [section.strip() for section in text.split('\n\n')]

seeds = re.findall(r'\b\d+\b', sections[0])
seeds = [int(seed) for seed in seeds]

def text_to_maps(section):
    lines = section.strip().splitlines()
    return_list = []
    for i, line in enumerate(lines):
        if i == 0:
            continue
        else:
            return_list.append([int(num) for num in line.split()])
    return return_list

se2so = text_to_maps(sections[1])
so2f = text_to_maps(sections[2])
f2w = text_to_maps(sections[3])
w2li = text_to_maps(sections[4])
li2t = text_to_maps(sections[5])
t2h = text_to_maps(sections[6])
h2lo = text_to_maps(sections[7])

def get_next_mapping(key, map, r=False):
    for line in map:
        dest = 0
        source = 1
        if r == True:
            dest = 1
            source = 0
        if key >= line[source] and key < line[source] + line[2]:
            return line[dest] + (key - line[source])
    return key

# print(seeds[0])
# print(get_next_mapping(seeds[0], se2so))

locations = []
for seed in seeds:
    location = get_next_mapping(get_next_mapping(get_next_mapping(get_next_mapping(get_next_mapping(get_next_mapping(get_next_mapping(seed, se2so), so2f), f2w), w2li), li2t), t2h), h2lo)
    locations.append(location)

part1_ans = min(locations)

end_time_1 = time.time()

new_seeds = []
for i in range(0, len(seeds), 2):
    new_seeds.append([seeds[i], seeds[i] + seeds[i+1]])


location = 0
seed_found = False
range_found = False
while seed_found == False:
    if range_found == True:
        location += 1
    try:
        seed = get_next_mapping(get_next_mapping(get_next_mapping(get_next_mapping(get_next_mapping(get_next_mapping(get_next_mapping(location, h2lo, r=True), t2h, r=True), li2t, r=True), w2li, r=True), f2w, r=True), so2f, r=True), se2so, r=True)
    except:
        continue
    for new_seed in new_seeds:
        if seed >= new_seed[0] and seed <= new_seed[1]:
            if range_found == False:
                range_found = True
                location -= 100000
                continue
            else:
                seed_found = True
    if range_found == False:
        location += 100000

part2_ans = location
end_time_2 = time.time()

part1_time = round((end_time_1-start_time_1) * 1000, 2)
part2_time = round((end_time_2-end_time_1) * 1000, 2)
print(f'Part 1: {part1_ans} ({part1_time} ms), Part 2: {part2_ans} ({part2_time} ms)')
