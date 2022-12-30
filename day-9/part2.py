class Point:
  def __init__(self, point):
    self.x = 0
    self.y = 0
    self.touched_points = []
    self.following_point = point

knots = []

head = Point(None)
knots.append(head)

for i in range(9):
  new_point = Point(knots[i])
  new_point.touched_points.append([0,0])
  knots.append(new_point)

knots.pop(0)

print(knots)

input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.rstrip() for line in lines if line.rstrip()]

for line in lines:
  commands = line.split(' ')
  for i in range(int(commands[1])):
      if commands[0] == 'U':
        head.y += 1
      if commands[0] == 'D':
        head.y -= 1
      if commands[0] == 'R':
        head.x += 1
      if commands[0] == 'L':
        head.x -= 1
      for knot in knots:
        if abs(knot.following_point.y - knot.y) > 1 and abs(knot.following_point.x - knot.x) > 1:
          if knot.following_point.y - knot.y > 0:
            knot.y += 1
          else:
            knot.y -= 1
          if knot.following_point.x - knot.x > 0:
            knot.x += 1
          else:
            knot.x -= 1
          knot.touched_points.append([knot.x, knot.y]) 
        elif abs(knot.following_point.y - knot.y) > 1 and abs(knot.following_point.x - knot.x) > 0:
          if knot.following_point.y - knot.y > 0:
            knot.y += 1
          else:
              knot.y -= 1
          knot.x = knot.following_point.x
          knot.touched_points.append([knot.x, knot.y]) 
        elif abs(knot.following_point.y - knot.y) > 0 and abs(knot.following_point.x - knot.x) > 1:
          if knot.following_point.x - knot.x > 0:
            knot.x += 1
          else:
            knot.x -= 1
          knot.y = knot.following_point.y
          knot.touched_points.append([knot.x, knot.y]) 
        elif abs(knot.following_point.y - knot.y) > 1 and abs(knot.following_point.x - knot.x) == 0:
          if knot.following_point.y - knot.y > 0:
            knot.y += 1
          else:
             knot.y -= 1
          knot.touched_points.append([knot.x, knot.y]) 
        elif abs(knot.following_point.y - knot.y) == 0 and abs(knot.following_point.x - knot.x) > 1:
          if knot.following_point.x - knot.x > 0:
            knot.x += 1
          else:
            knot.x -= 1
          knot.touched_points.append([knot.x, knot.y]) 

print(head.x)
print(head.y)
for knot in knots:
  print(knot.touched_points)
  print()
  print()


res = []
[res.append(x) for x in knots[8].touched_points if x not in res]
print(len(res))

