input_file = open('input.txt', 'r')

lines = input_file.readlines()

groups = zip(*[iter(lines)]*3)

total_points = 0

for group in groups:
    for letter in group[0]:
        if letter in group[1]:
            if letter in group[2]:
                common_letter = letter
                break
    ascii_val = ord("".join(common_letter))
    if ascii_val > 96 :
        priority = ascii_val - 96
        total_points += priority
    else:
        priority = ascii_val - 38
        total_points += priority

print(total_points)