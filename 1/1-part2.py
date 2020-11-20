import math

TARGET = 2020

def find_pair(target, low, high):
    while (high > low):
        if (entries[high] + entries[low] == target):
            return [entries[low], entries[high]]
        higher_bound = target - entries[low]
        lower_bound = target - entries[high]            
        while (entries[low] < lower_bound):
            low += 1
        while (entries[high] > higher_bound):
            high -= 1
    return None

with open('input.txt') as f:
    entries = f.read().split('\n')
    entries = sorted([int(x) for x in entries])
    for third in range(len(entries)-2):
        result = find_pair(TARGET - entries[third], third+1, len(entries)-1)
        if result:
            break
    if result:
        result.append(entries[third])
        print(f"Entries that add to {TARGET} are: {result}")
        print(f"Product is: {math.prod(result)}")
    else:
        print(f"No trio found which sum to {TARGET}")