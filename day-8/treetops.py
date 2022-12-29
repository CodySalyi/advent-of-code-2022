input_file = open('day-8/input.txt', 'r')
lines = input_file.readlines()
lines = [line.rstrip() for line in lines if line.rstrip()]
lines = [[*line] for line in lines]

column = 1
row = 1

up = True
down = True
left = True
right = True

visible_trees = 0

while row <= len(lines) - 2:
  while column <= len(lines[row]) - 2:
    #check right
    i = column + 1
    while i <= len(lines[row]) - 1 and right:
      if lines[row][column] <= lines[row][i]:
        right = False
      else:
        i = i+1
    #check left
    i = column - 1
    while i >= 0 and left:
      if lines[row][column] <= lines[row][i]:
        left = False
      else:
        i = i-1
    #check down
    i = row + 1
    while i <= len(lines) - 1 and down:
      if lines[row][column] <= lines[i][column]:
        down = False
      else:
        i = i+1
    #check up
    i = row - 1
    while i >= 0 and up:
      if lines[row][column] <= lines[i][column]:
        up = False
      else:
        i = i-1
    if up or down or left or right:
      visible_trees = visible_trees + 1
    column = column + 1
    up = True
    down = True
    left = True
    right = True
  row = row+1
  column = 1

visible_trees = visible_trees + (2*len(lines)) + (2*(len(lines)-2))

print(visible_trees)



