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
    result = find_pair(TARGET, 0, len(entries)-1)
    if result:
        print(f"Entries that add to {TARGET} are: {result}")
        print(f"Product is: {math.prod(result)}")
    else:
        print(f"No pair found which sum to {TARGET}")