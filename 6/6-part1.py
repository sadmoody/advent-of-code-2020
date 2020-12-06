with open('input.txt') as f:
    group_answers = f.read().split('\n\n')
    total_yesses = 0
    for group_answer in group_answers:
        unique_yesses = set(group_answer.replace('\n', ''))
        total_yesses += len(unique_yesses)
    print(f"Total number of yesses per group: {total_yesses}")
