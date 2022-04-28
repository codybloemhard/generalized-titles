import sys
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
            rule.append((True, word))
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
    data = path.read_text()
    current = root
    segments = os.fspath(path).split('/')
    last = len(segments) - 1
    for i, segment in enumerate(segments[1:]):
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

print_tree(root, 'root', 0)
