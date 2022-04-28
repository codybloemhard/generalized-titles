import sys
import random
import pathlib
import os

# need input file

if len(sys.argv) < 2:
    print('No file argument given for the rules')
    exit()

# parse rules

rules = []
file = open(sys.argv[1], "r")

for line in file:
    if len(line) == 0:
        continue
    if line[0].isspace():
        continue
    words = line.split(' ')
    rule = []
    for word in words:
        if len(word) == 0:
            continue
        word = word.replace('\n', '')
        if word[0] == '/':
            rule.append((True, word.replace('/', '')))
        else:
            rule.append((False, word))
    if len(rule) > 0:
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

    for (substitute, string) in rule:
        if substitute:
            cat = find_category(string, root)
            if cat is None:
                #print('____')
                #print('Could not find substitution for "/' + string + '" in the data tree!')
                res += '____: '
                res += 'Could not find substitution for "/' + string + '" in the data tree!'
                return res
            item = pick_item(cat)
            res += item + ' '
            #print(item + ' ', end = '')
        else:
            res += string + ' '
            #print(string + ' ', end = '')
    return res

l = 1
if len(sys.argv) > 2:
    l = int(sys.argv[2])

for _ in range(l):
    print(generate(rules, root))

