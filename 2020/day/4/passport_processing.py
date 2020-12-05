def get_passports_from_input(lines):
    passports = []
    passport = {}
    for line in lines:
        if line == '':
            passports.append(passport)
            passport = {}
        else:
            pairs = line.strip().split(' ')
            for pair in pairs:
                key, value = pair.split(':')
                passport[key] = value
    passports.append(passport)
    return passports

def is_height_valid(height):
    height_unit = height[-2:]
    if height_unit == 'cm':
        return 150 <= int(height[:-2]) <= 193
    elif height_unit == 'in':
        return 59 <= int(height[:-2]) <= 76
    return False

def is_hair_colour_valid(hair_colour):
    if hair_colour[0] != '#':
        return False
    for character in hair_colour[1:]:
        if character not in '0123456789abcdef':
            return False
    return True

def is_passport_valid(passport):
    birth_year = 'byr' in passport and 1920 <= int(passport['byr']) <= 2002
    issue_year = 'iyr' in passport and 2010 <= int(passport['iyr']) <= 2020
    expiration_year = 'eyr' in passport and 2020 <= int(passport['eyr']) <= 2030
    height = 'hgt' in passport and is_height_valid(passport['hgt'])
    hair_colour = 'hcl' in passport and is_hair_colour_valid(passport['hcl'])
    eye_colour = 'ecl' in passport and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    passport_id = 'pid' in passport and passport['pid'].isnumeric() and len(passport['pid']) == 9

    return birth_year and issue_year and expiration_year and height and hair_colour and eye_colour and passport_id

def count_valid_passports(passports):
    count = 0
    for passport in passports:
        if is_passport_valid(passport):
            count += 1
    return count

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        print(len(lines))
        passports = get_passports_from_input(lines)
        count = count_valid_passports(passports)
        print('{} passports are valid out of a total of {}'.format(count, len(passports)))
