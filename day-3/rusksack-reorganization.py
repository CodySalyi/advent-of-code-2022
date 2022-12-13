input_file = open('input.txt', 'r')

lines = input_file.readlines()

total_points = 0

for line in lines:
    middle_index = len(line) // 2
    word1 = line[:middle_index]
    word2 = line[middle_index:]
    common_letter = set(word1).intersection(set(word2))
    ascii_val = ord("".join(common_letter))
    if ascii_val > 96 :
        priority = ascii_val - 96
        total_points += priority
    else:
        priority = ascii_val - 38
        total_points += priority

print(total_points)