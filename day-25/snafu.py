def decode_snafu(input):
  char_list = list(input)
  char_list.reverse()
  total = 0
  loops = 0
  for char in char_list:
    match char:
        case '=': #-2
          total = total + (pow(5,loops)*-2)
          loops = loops+1
        case '-': #-1
          total = total + (pow(5,loops)*-1)
          loops = loops+1
        case '0': #0
          loops = loops+1
        case '1': #1
          total = total + pow(5,loops)
          loops = loops+1
        case '2': #2
          total = total + (pow(5,loops)*2)
          loops = loops+1
  return total

def encode_snafu(input):
  char_list = []
  total = 1
  loops = 0

  while total < input:
    total = total * 5
    loops = loops + 1

  if input/pow(5,loops) <= 0.50:
    loops = loops - 1
  
  while loops >= 0:
    place = round(input/pow(5,loops))
    match place:
      case -2:
        char_list.append('=')
        input = input - (pow(5,loops)*-2)
        loops = loops - 1
      case -1:
        char_list.append('-')
        input = input - (pow(5,loops)*-1)
        loops = loops - 1
      case 0:
        char_list.append('0')
        loops = loops - 1
      case 1:
        char_list.append('1')
        input = input - pow(5,loops)
        loops = loops - 1
      case 2:
        char_list.append('2')
        input = input - (pow(5,loops)*2)
        loops = loops - 1
  return char_list


input_file = open('input.txt', 'r')

total_sum = 0
lines = input_file.readlines()
lines = [line.rstrip() for line in lines if line.rstrip()]

for line in lines:
  result = decode_snafu(line)
  total_sum = total_sum + result

print(total_sum)
answer = encode_snafu(total_sum)
str = ""
print(str.join(answer))

