with open('input.txt') as f:
    entries = f.read().split('\n')
    count = 0
    for entry in entries:
        [limits, letter, password] = entry.split(' ')
        [low, high] = limits.split('-')
        low, high = int(low), int(high)
        letter = letter[0]
        occurences = password.count(letter)
        if (occurences >= low and occurences <= high):
            count += 1
    print(f"Total number of correct passwords: {count}")
