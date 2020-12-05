def is_password_valid(lower_bound, upper_bound, character, password):
    count = 0
    for char in password:
        if char == character:
            count += 1
    return lower_bound <= count <= upper_bound

def parse_line(line):
    parts = line.split(' ')
    bounds = parts[0].split('-')
    lower_bound = int(bounds[0])
    upper_bound = int(bounds[1])
    character = parts[1][0]
    password = parts[2].strip()
    return (lower_bound, upper_bound, character, password)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [parse_line(line) for line in f.readlines()]
        count = 0
        for line in lines:
            if is_password_valid(*line):
                count += 1
        print('{} passwords are valid out of a total of {}'.format(count, len(lines)))