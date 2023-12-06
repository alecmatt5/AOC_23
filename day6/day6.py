import time
# time held = speed (i.e. time held = 4 ms, speed = 4 mm/ms)
# times_1 = [59, 70, 78, 78]
# distances_1 = [430, 1218, 1213, 1276]
# times_2 = [59707878]
# distances_2 = [430121812131276]

def run_races(times, distances):
    ans = 1
    for i, tot_time in enumerate(times):
        count = 0
        for time_held in range(tot_time):
            time_traveled = tot_time - time_held
            speed = time_held
            distance_travelled = speed * time_traveled
            if distance_travelled > distances[i]:
                count += 1
        ans *= count
    return ans

start_time_1 = time.time()
with open('day6.txt', 'r') as file:
    for line in file:
        if line.startswith('Time:'):
            times_1 =[int(value) for value in line.split()[1:]]
        if line.startswith('Distance:'):
            distances_1 = [int(value) for value in line.split()[1:]]
part1_ans = run_races(times_1, distances_1)
end_time_1 = time.time()
part1_time = round((end_time_1-start_time_1) * 1000, 2)

start_time_2 = time.time()
times_2 = [int(''.join(map(str, times_1)))]
distances_2 = [int(''.join(map(str, distances_1)))]
part2_ans = run_races(times_2, distances_2)
end_time_2 = time.time()
part2_time = round((end_time_2-start_time_2) * 1000, 2)

print(f'Part 1: {part1_ans} ({part1_time} ms), Part 2: {part2_ans} ({part2_time} ms)')
