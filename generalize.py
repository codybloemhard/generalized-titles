import sys
import random
import pathlib
import os
from dataclasses import dataclass

# need input file

if len(sys.argv) < 2:
    print('No file argument given for the rules')
    exit()

# parse rules

prerules = []
file = open(sys.argv[1], "r")

for line in file:
    if len(line) == 0:
        continue

    rule = []
    segment = ''
    sub = False

    for char in line:
        if char == '{':
            if segment != '':
                rule.append((segment, False))
                segment = ''
            sub = True
        elif char == '}':
            if not sub:
                print('Closing "}" without opening "{" in "' + line + '"')
                exit()
            rule.append((segment, True))
            segment = ''
        elif char != '\n':
            segment += char

    if segment != '':
        rule.append((segment, False))

    if len(rule) > 0:
        prerules.append(rule)

class Segment:
    """Substitution rule segment"""

@dataclass
class String(Segment):
    string: str

@dataclass
class Sub(Segment):
    og: str
    sub: str
    first_letter: str
    unique: bool

rules = []
for prerule in prerules:
    rule = []
    for (segment, is_sub) in prerule:
        if not is_sub:
            rule.append(String(string = segment))
        else:
            fields = segment.split(',')
            if len(fields) < 2:
                print('Not enough fields in sub: "{' + segment + '}" in rule: "' + str(prerule) + '"')
                exit()
            first = None
            _unique = False
            for field in fields[2:]:
                if len(field) == 1: # first letter
                    first = field.lower()
                if field == 'unique':
                    _unique = True
            rule.append(Sub(
                og = fields[0],
                sub = fields[1],
                first_letter = first,
                unique = _unique
            ))
    rules.append(rule)

# build data tree

class Tree:
    def __init__(self, data):
        self.data = data
        self.children = {}

root = Tree(None)

for path in pathlib.Path('data').rglob('*.sub'):
    data = list(filter(lambda x: x != '', path.read_text().split('\n')))
    current = root
    segments = os.fspath(path).split('/')
    last = len(segments) - 2
    for i, segment in enumerate(segments[1:]):
        segment = segment.replace('.sub', '')
        if i is not last:
            if not segment in current.children:
                current.children[segment] = Tree(None)
            current = current.children[segment]
        else:
            current.children[segment] = Tree(data)

def print_tree(tree, name, depth):
    pad = depth * ' '
    if tree.data is None:
        print(pad + name)
        for name, child in tree.children.items():
            print_tree(child, name, depth + 1)
    else:
        print(pad + name + ' = DATA')

# print_tree(root, 'root', 0)

def find_category(category, tree):
    if tree.data is None:
        for name, child in tree.children.items():
            if name == category:
                return child
            else:
                res = find_category(category, child)
                if res is not None:
                    return res
    else:
        return None
    return None

def pick_item(tree):
    if tree.data is None:
        l = len(tree.children)
        i = 0
        if l > 1:
            i = random.randint(0, l - 1)
        return pick_item(list(tree.children.values())[i])
    else:
        l = len(tree.data)
        i = random.randint(0, l - 1)
        r = tree.data[i]
        return r

# pick a rule

def generate(rules, root):
    res = ''
    rule = rules[random.randint(0, len(rules) - 1)]
    subs = []

    for segment in rule:
        if isinstance(segment, Sub):
            cat = find_category(segment.sub, root)
            if cat is None:
                res += '____: '
                res += 'Could not find substitution for "/' + segment.sub + '" in the data tree!'
                return res
            item = pick_item(cat)
            i = 1000
            while i > 0 and ((segment.first_letter != None and item[0].lower() != segment.first_letter) or (segment.unique and item in subs)):
                i -= 1
                item = pick_item(cat)
            res += item
            subs.append(item)
        else:
            res += segment.string
    return res

l = 1
if len(sys.argv) > 2:
    l = int(sys.argv[2])

for _ in range(l):
    print(generate(rules, root))

