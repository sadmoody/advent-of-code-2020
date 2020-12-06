with open('input.txt') as f:
    group_answers = f.read().split('\n\n')
    total_all_yesses = 0
    for group_answer in group_answers:
        occurences = {'\n': 1} 
        for character in group_answer: 
            if character in occurences: 
                occurences[character] += 1
            else: 
                occurences[character] = 1
        all_yesses = []
        for character in occurences:
            if character == '\n':
                continue
            if occurences[character] == occurences['\n']:
                all_yesses.append(character)
        total_all_yesses += len(all_yesses)
    print(f"Total number of all-yesses per group: {total_all_yesses}")
