import re, itertools

rules = []
bags = []

class Rule:
    def __init__(self, bag, contains, quantity):
        self.bag = bag
        self.contains = contains
        self.quantity = quantity

def bags_needed_for(current_bag):
    links = list(filter(lambda rule: rule.bag == current_bag, rules))
    if links:
        return 1 + sum(map(lambda link: link.quantity * bags_needed_for(link.contains), links))
    return 1

with open('input.txt') as f:
    text_rules = f.read().split('\n')
    for text_rule in text_rules:
        [current_bag, suffix] = text_rule.split(' bags contain')
        if current_bag not in bags:
            bags.append(current_bag)
        inner_bags = re.findall(r'(\d+)\s(\w+\s\w+)\sbag', suffix)
        if inner_bags:
            for inner_bag in inner_bags:
                quantity = int(inner_bag[0])
                bag = inner_bag[1]
                if bag not in bags:
                    bags.append(bag)
                rules.append(Rule(current_bag, bag, quantity))
    # We subtract 1 for the initial shiny gold bag
    print(f"Total number of bags required to take a shiny gold bag: {bags_needed_for('shiny gold') - 1}")