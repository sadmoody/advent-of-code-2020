REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
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
        if all(field in passport for field in REQUIRED_FIELDS):
            valid_passports += 1
    
    print(f"Total number of valid passports: {valid_passports}")
