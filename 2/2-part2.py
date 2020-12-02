with open('input.txt') as f:
    entries = f.read().split('\n')
    count = 0
    for entry in entries:
        [positions, letter, password] = entry.split(' ')
        [pos1, pos2] = positions.split('-')
        pos1, pos2 = int(pos1)-1, int(pos2)-1
        letter = letter[0]
        correct = (password[pos1] == letter) != (password[pos2] == letter)
        if (correct):
            count += 1
    print(f"Total number of correct passwords: {count}")
