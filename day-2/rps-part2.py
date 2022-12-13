input_file = open('rock-paper-scissors-input.txt', 'r')

lines = input_file.readlines()

total_points = 0
totals = []

for line in lines:
    opponent = line[0]
    player = line[2]
    match opponent:
        case 'A': #rock
            match player:
                case 'X': #lose
                    total_points += (3+0)
                case 'Y': #tie
                    total_points += (1+3)
                case 'Z': #win
                    total_points += (2+6)

        case 'B': #paper
            match player:
                case 'X':
                    total_points += (1+0)
                case 'Y':
                    total_points += (2+3)
                case 'Z':
                    total_points += (3+6)
                    
        case 'C': #scissors
            match player:
                case 'X':
                    total_points += (2+0)
                case 'Y':
                    total_points += (3+3)
                case 'Z':
                    total_points += (1+6)

print(total_points)