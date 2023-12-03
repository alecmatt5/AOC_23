import re
pattern = r'\b\d+\b'
grid = []
y_vals = [-1, 0, 1]
check_vals = ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sum1 = 0
num_locations = []
ast_dict = {}

with open('day3.txt', 'r') as file:
    for row_num, line in enumerate(file):
        matches = re.finditer(pattern, line)
        num_location = [[row_num, match.start(), len(match.group()), int(match.group())] for match in matches]
        num_locations.extend(num_location)
        row = list(line.strip())
        grid.append(row)

for num in num_locations:
    row = num[0]
    column = num[1]
    num_len = num[2]
    column_last_digit = column + num_len
    for y in y_vals:
        found = False
        if row + y == -1 or row + y > row_num:
            continue
        for x in range(-1, num_len + 1):
            if column + x == -1 or column + x > row_num:
                continue
            if grid[row + y][column + x] == '*':
                ast_loc = (row + y, column + x)
                if ast_loc in ast_dict:
                    if num[3] in ast_dict[ast_loc]:
                        pass
                    else:
                        ast_dict[ast_loc].append(num[3])
                else:
                    ast_dict[ast_loc] = [num[3]]
            if grid[row + y][column + x] in check_vals:
                continue
            else:
                sum1 += num[3]
                found = True
                break
        if found == True:
            break

sum2 = sum([value[0] * value[1] for key, value in ast_dict.items() if len(value) == 2])

print(f'Part 1: {sum1}, Part 2: {sum2}')
