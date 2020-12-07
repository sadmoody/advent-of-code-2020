import re, itertools

rules = []
bags = []

class Rule:
    def __init__(self, bag, contains, quantity):
        self.bag = bag
        self.contains = contains
        self.quantity = quantity

def find_bags(current_bag):
    links = list(filter(lambda rule: rule.contains == current_bag, rules))
    return list(set([link.bag for link in links] + list(itertools.chain.from_iterable(list(map(lambda link : find_bags(link.bag), links))))))


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
    print(f"Total number of unique bags which could contain shiny gold bags: {len(find_bags('shiny gold'))}")