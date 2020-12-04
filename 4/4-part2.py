import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
HAIR_COLOURS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
with open('input.txt') as f:
    entries = f.read().split('\n\n')
    entries = [x.replace('\n', ' ') for x in entries]
    passports = []
    for entry in entries:
        fields = entry.split(' ')
        passport = {}
        for field in fields:
            [key, value] = field.split(':')
            passport[key] = value
        passports.append(passport)

    valid_passports = 0
    for passport in passports:
        if not all(field in passport for field in REQUIRED_FIELDS):
            continue
        
        birth_year = int(passport['byr'])
        if not 1920 <= birth_year <= 2002:
            continue

        issue_year = int(passport['iyr'])
        if not 2010 <= issue_year <= 2020:
            continue

        expiration_year = int(passport['eyr'])
        if not 2020 <= expiration_year <= 2030:
            continue

        height = int(passport['hgt'][:-2])
        height_unit = passport['hgt'][-2:]
        if not (height_unit == 'cm' and 150 <= height <= 193) and not (height_unit == 'in' and 59 <= height <= 76):
            continue

        hair_colour_match = re.search(r"\A#[a-f0-9]{6}\Z", passport['hcl'])
        if not hair_colour_match:
            continue

        if passport['ecl'] not in HAIR_COLOURS:
            continue

        passport_id_match = re.search(r"\A[0-9]{9}\Z", passport['pid'])
        if not passport_id_match:
            continue

        valid_passports += 1
    
    print(f"Total number of valid passports: {valid_passports}")
