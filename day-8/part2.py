input_file = open('day-8/input.txt', 'r')
lines = input_file.readlines()
lines = [line.rstrip() for line in lines if line.rstrip()]
lines = [[*line] for line in lines]

column = 1
row = 1

up = 0
down = 0
left = 0
right = 0

max_score = 0

while row <= len(lines) - 2:
  while column <= len(lines[row]) - 2:
    #check right
    i = column + 1
    while i <= len(lines[row]) - 1 and right == 0:
      if lines[row][column] <= lines[row][i]:
        right = i - column
        i = i+1
      else:
        i = i+1
    if right == 0:
      right = len(lines[row]) - column - 1
    #check left
    i = column - 1
    while i >= 0 and left == 0:
      if lines[row][column] <= lines[row][i]:
        left = column - i
        i = i-1
      else:
        i = i-1
    if left == 0:
        left = column
    #check down
    i = row + 1
    while i <= len(lines) - 1 and down == 0:
      if lines[row][column] <= lines[i][column]:
        down = i - row
        i = i+1
      else:
        i = i+1
    if down == 0:
      down = len(lines) - row - 1
    #check up
    i = row - 1
    while i >= 0 and up == 0:
      if lines[row][column] <= lines[i][column]:
        up = row - i
        i = i-1
      else:
        i = i-1
    if up == 0:
      up = row
    
    scenic_score = up * down * left * right
    if scenic_score > max_score:
      max_score = scenic_score

    column = column + 1
    up = 0
    down = 0
    left = 0
    right = 0
  row = row+1
  column = 1


print(max_score)



