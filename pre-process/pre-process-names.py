import csv

dataset = open('name_gender_dataset.csv')
reader = csv.reader(dataset, delimiter=',')
first = True

names_male = []
names_female = []


for row in reader:
    if first:
        first = False
        continue

    if row[1] == "M":
        names_male.append(row[0])
    else:
        names_female.append(row[0])

def write_to_file(names, filename):
    f = open(filename, "w")
    for name in names:
        f.write(name + "\n")
    f.close()

write_to_file(names_male, "names-male")
write_to_file(names_female, "names-female")
