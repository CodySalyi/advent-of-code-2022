import ast

def recurse(left, right):
  i = 0
  while True:
    if i < len(left):
      if i < len(right):
        if isinstance(left[i], int) and isinstance(right[i], int):
          if left[i] < right[i]:
            return True
          if left[i] > right[i]:
            return False
          if left[i] == right[i]:
            i += 1
        elif isinstance(left[i], list) and isinstance(right[i], list):
          val = recurse(left[i], right[i])
          if val == "next":
            i += 1
          elif val:
            return True
          elif not val:
            return False
        elif isinstance(left[i], int) and isinstance(right[i], list):
          val = recurse([left[i]], right[i])
          if val == "next":
            i += 1
          elif val:
            return True
          elif not val:
            return False
        elif isinstance(left[i], list) and isinstance(right[i], int):
          val = recurse(left[i], [right[i]])
          if val == "next":
            i += 1
          elif val:
            return True
          elif not val:
            return False
      else:
        return False
    else:
      if i < len(right):
        return True
      else:
        return "next"

input_file = open('day-13/test.txt', 'r')

total_sum = 0
lines = input_file.readlines()
lines = [line.rstrip() for line in lines if line.rstrip()]
for i in range(0, len(lines), 2):
  group = lines[i:i+2]

  left = ast.literal_eval(group[0])
  right = ast.literal_eval(group[1])

  result = recurse(left, right)

  if result:
    print(int(i/2)+1)
    total_sum += int(i/2)+1

print(total_sum)
