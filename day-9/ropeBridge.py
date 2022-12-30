class Point:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.touched_points = []

head = Point()
tail = Point()
tail.touched_points.append([0,0])

input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.rstrip() for line in lines if line.rstrip()]

for line in lines:
  commands = line.split(' ')

  if commands[0] == 'U':
    for i in range(int(commands[1])):
      head.y += 1
      if abs(head.y - tail.y) > 1:
        tail.y = head.y - 1
        tail.x = head.x
        tail.touched_points.append([tail.x, tail.y])

  if commands[0] == 'D':
    for i in range(int(commands[1])):
      head.y -= 1
      if abs(head.y - tail.y) > 1:
        tail.y = head.y + 1
        tail.x = head.x
        tail.touched_points.append([tail.x, tail.y])
      

  if commands[0] == 'R':
    for i in range(int(commands[1])):
      head.x += 1
      if abs(head.x - tail.x) > 1:
        tail.x = head.x - 1
        tail.y = head.y
        tail.touched_points.append([tail.x, tail.y])

  if commands[0] == 'L':
    for i in range(int(commands[1])):
      head.x -= 1
      if abs(head.x - tail.x) > 1:
        tail.x = head.x + 1
        tail.y = head.y
        tail.touched_points.append([tail.x, tail.y])

  print(head.x)
  print(head.y)

print(head.x)
print(head.y)
print(tail.touched_points)


res = []
[res.append(x) for x in tail.touched_points if x not in res]
print(len(res))

