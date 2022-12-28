def checkMarker(unit):
  for x in range(0,3):
    char_count = unit.count(unit[x])
    if char_count > 1:
      return False
  return True

input_file = open('input.txt', 'r')
lines = input_file.readlines()
line = lines[0]

found = False
place = 0
while not found:
  unit = line[place:place+4]
  result = checkMarker(unit)
  if result:
    break
  place = place + 1

print(place+4)