import time

grid = []
empty_rows = []
empty_cols = []
with open('day11.txt', 'r') as file:
    for i, line in enumerate(file):
        row = list(line.strip())
        if '#' not in row:
            empty_rows.append(i)
        grid.append(row)

num_cols_added = 0
for col in range(len(grid[0])):
    empty_col = True
    for row in grid:
        if row[col] == '#':
            empty_col = False
            break
    if empty_col == True:
        empty_cols.append(col)

galaxy_coords = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '#':
            galaxy_coords.append([row, col])

def calc_total_steps(galaxy_coords, multiplier):
    total_distance = 0
    for i in range(len(galaxy_coords)):
        for j in range(i+1, len(galaxy_coords)):
            row1, col1 = galaxy_coords[i]
            row2, col2 = galaxy_coords[j]
            num_empty_cols = 0
            num_empty_rows = 0
            for col_num in empty_cols:
                if col1 <= col2:
                    if col_num in list(range(col1, col2)):
                        num_empty_cols += 1
                else:
                    if col_num in list(range(col2, col1)):
                        num_empty_cols += 1
            for row_num in empty_rows:
                if row1 <= row2:
                    if row_num in list(range(row1, row2)):
                        num_empty_rows += 1
                else:
                    if row_num in list(range(row2, row1)):
                        num_empty_rows += 1
            x_dist = abs(col2 - col1) + num_empty_cols * (multiplier - 1)
            y_dist = abs(row2 - row1) + num_empty_rows * (multiplier - 1)
            total_distance += (x_dist + y_dist)
    return total_distance

start_time_1 = time.time()
part1_ans = calc_total_steps(galaxy_coords, multiplier=2)
end_time_1 = time.time()
part2_ans = calc_total_steps(galaxy_coords, multiplier=1000000)
end_time_2 = time.time()

part1_time = round((end_time_1-start_time_1) * 1000, 2)
part2_time = round((end_time_2-end_time_1) * 1000, 2)
print(f'Part 1: {part1_ans} ({part1_time} ms), Part 2: {part2_ans} ({part2_time} ms)')
