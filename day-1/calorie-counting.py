input_file = open('calorie-counting-input.txt', 'r')

lines = input_file.readlines()

sum = 0
totals = []

for line in lines:

    if(line == '\n'):
      print("{}: {}".format(len(totals), sum))
      totals.append(sum)
      sum = 0
    else:
      sum += int(line.strip())

totals.append(sum)

max_calories = max(totals)

print("Max Calories: {}".format(max_calories))