input_file = open('input.txt', 'r')

lines = input_file.readlines()
counter = 0
for line in lines:
    assignments = line.split(",")
    assignment1 = assignments[0].split("-")
    assignment1range = set(range(int(assignment1[0]), int(assignment1[1])+1))

    assignment2 = assignments[1].split("-")
    assignment2range = set(range(int(assignment2[0]), int(assignment2[1])+1))

    intersection = assignment1range.intersection(assignment2range)

    if intersection:
        counter+=1

print(counter)