import ast
import functools

def recurse(leftstr, rightstr):
  if isinstance(leftstr, str): left = ast.literal_eval(leftstr)
  else: left = leftstr
  if isinstance(rightstr, str): right = ast.literal_eval(rightstr)
  else: right = rightstr
  
  i = 0
  while True:
    if i < len(left):
      if i < len(right):
        if isinstance(left[i], int) and isinstance(right[i], int):
          if left[i] < right[i]:
            return 1
          if left[i] > right[i]:
            return -1
          if left[i] == right[i]:
            i += 1
        elif isinstance(left[i], list) and isinstance(right[i], list):
          val = recurse(left[i], right[i])
          if val == "next":
            i += 1
          elif val == 1:
            return 1
          elif val == -1:
            return -1
        elif isinstance(left[i], int) and isinstance(right[i], list):
          val = recurse([left[i]], right[i])
          if val == "next":
            i += 1
          elif val == 1:
            return 1
          elif val == -1:
            return -1
        elif isinstance(left[i], list) and isinstance(right[i], int):
          val = recurse(left[i], [right[i]])
          if val == "next":
            i += 1
          elif val == 1:
            return 1
          elif val == -1:
            return -1
      else:
        return -1
    else:
      if i < len(right):
        return 1
      else:
        return "next"

input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.rstrip() for line in lines if line.rstrip()]
lines.append("[[2]]")
lines.append("[[6]]")

result = sorted(lines, key=functools.cmp_to_key(recurse), reverse=True)

packet2 = result.index("[[2]]") +1
packet6 = result.index("[[6]]") +1
decoderkey= packet2 * packet6
print(decoderkey)
