import sys

if len(sys.argv) < 3:
    print('Give an input and output file!')
    exit()

dataset = open(sys.argv[1], 'r')

res = []

for line in dataset.readlines():
    res.append(line.capitalize())

f = open(sys.argv[2], 'w')
for line in res:
    f.write(line)
f.close()

