import re
file = open('Test.txt')
for line in file:
    line = line.rstrip()
    if re.search('From', line):
        print(line)
file.close()

file2 = open('Test.txt')
for line in file2:
    line = line.rstrip()
    if re.search('^Today', line):
        print(line)