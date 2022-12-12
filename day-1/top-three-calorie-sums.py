input_file = open('calorie-counting-input.txt', 'r')

lines = input_file.readlines()

summation = 0
totals = []

for line in lines:

    if(line == '\n'):
      print("{}: {}".format(len(totals), summation))
      totals.append(summation)
      summation = 0
    else:
      summation += int(line.strip())

totals.append(summation)

top_three = sorted(totals, reverse=True)[:3]
summation = sum(top_three)
print(summation)