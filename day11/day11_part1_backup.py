import time

grid = []
with open('day11.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        if '#' not in row:
            grid.append(row)
        grid.append(row)

num_cols_added = 0
for col in range(len(grid[0])):
    col += num_cols_added
    empty_col = True
    for row in grid:
        try:
            if row[col] == '#':
                empty_col = False
                break
        except:
            break
    if empty_col == True:
        for row in grid:
            row.insert(col, '.')
        num_cols_added += 1

galaxy_coords = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '#':
            galaxy_coords.append([row, col])

def calc_dist_steps(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return (abs(x2-x1) + abs(y2-y1))

total_distance = 0
for i in range(len(galaxy_coords)):
    for j in range(i+1, len(galaxy_coords)):
        coord1 = galaxy_coords[i]
        coord2 = galaxy_coords[j]
        total_distance += calc_dist_steps(coord1, coord2)
print(total_distance)
# start_time_1 = time.time()
# end_time_1 = time.time()
# end_time_2 = time.time()

# part1_time = round((end_time_1-start_time_1) * 1000, 2)
# part2_time = round((end_time_2-end_time_1) * 1000, 2)
# print(f'Part 1: {part1_ans} ({part1_time} ms), Part 2: {part2_ans} ({part2_time} ms)')
