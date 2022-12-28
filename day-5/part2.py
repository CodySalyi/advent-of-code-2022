#Read file and split into yard and directions
input_file = open('input.txt', 'r')
total_sum = 0
lines = input_file.readlines()
first_list = lines[:lines.index('\n')]
second_list = lines[lines.index('\n')+1:]

#Convert first list into one array of characters
all_chars = []
first_list.reverse()
first_line = list(first_list[0])
first_line = first_line[1::4]
first_line.reverse()
total_bays = first_line[0]
for line in first_list:
  line_chars = list(line)
  line_chars = line_chars[1::4]
  for char in line_chars:
    all_chars.append(char)

#Parse first list into yard of bays
yard = []
while_bays = int(total_bays) - 1
while while_bays >= 0:
  bay = all_chars[while_bays::(int(total_bays))]
  bay[:] = (value for value in bay if value != ' ')

  while_bays = while_bays - 1
  yard.append(bay)
yard.reverse()

#Parse second list of directions
directions = []
for line in second_list:
  line_chars = (line.strip()).split(' ')
  del line_chars[0::2]
  directions.append(line_chars)

#move algorithm
crane = []
for direction in directions:
  loops = int(direction[0])
  from_bay = int(direction[1])-1
  to_bay = int(direction[2])-1
  while loops > 0:
    transfer = yard[from_bay].pop()
    crane.append(transfer)
    loops = loops -1
  crane.reverse()
  yard[to_bay].extend(crane)
  crane = []

#Get top of each stack
answer = []
for bay_column in yard:
  bay_column.reverse()
  answer.append(bay_column[0])

#Convert to friendly string
str = ""
print(str.join(answer) )