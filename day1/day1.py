# PART 1
'''The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and
the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?'''

sum1 = 0
with open('day1.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        nums = ''.join(filter(str.isdigit, line))
        sum1 = sum1 + int(nums[0] + nums[-1])
print(sum1)

# PART 2
'''Your calculation isn't quite right. It looks like some of the digits are actually
spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?'''

sum2 = 0
# Keeping the first letter before the number and the last letter after the number solves the issue of when a
# character is being used for two diffent words (i.e. twone = 21, eighthree = 83)
digits_map = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e',
              'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}
with open('day1.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        for word, dig in digits_map.items():
            line = line.replace(word, dig)
        nums = ''.join(filter(str.isdigit, line))
        sum2 = sum2 + int(nums[0] + nums[-1])
print(sum2)
