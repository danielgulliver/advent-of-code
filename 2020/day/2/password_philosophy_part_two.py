def is_password_valid(position_one, position_two, character, password):
    return (password[position_one - 1] == character) != (password[position_two - 1] == character)

def parse_line(line):
    parts = line.split(' ')
    bounds = parts[0].split('-')
    position_one = int(bounds[0])
    position_two = int(bounds[1])
    character = parts[1][0]
    password = parts[2].strip()
    return (position_one, position_two, character, password)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [parse_line(line) for line in f.readlines()]
        count = 0
        for line in lines:
            if is_password_valid(*line):
                count += 1
        print('{} passwords are valid out of a total of {}'.format(count, len(lines)))