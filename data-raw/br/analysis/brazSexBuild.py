# Author: Luke Sonnet
# Purpose: Takes raw candidate from 1998-2014 in Brazil, strips out the first
#          word in the name field, records the sex, and saves it in a large csv
#          file. I can use numeric indexing because the TSE saw fit to
#          standardize these files (bless them).
#
# Python v: 3.5.4

from os import walk
import csv

firstNames = {}

def readNames(dir):
    """Loads the files, records the names, and counts the sexes"""
    for root, dirs, files in walk(path):
        for file in files:
            if file.endswith(('.txt', '.csv')):
                f = csv.reader(open(root + '/' + file, 'r', encoding='ISO-8859-1'), delimiter=';')
                for n, i in enumerate(f):
                    if n != 0:
                        # Get first name only as everything preceding first space
                        fname = i[10].split(" ")[0]

                        fname = fname.replace('`', '')
                        fname = fname.replace(',', '')
                        fname = fname.replace(']', '')

                        # if name exists, add to it, else create name
                        if not fname in firstNames.keys():
                            firstNames[fname] = [1, 0, 0]
                        else:
                            firstNames[fname][0] += 1
                        # males are '2', females are '4'
                        if i[28] == '2':
                            firstNames[fname][2] += 1
                        elif i[28] == '4':
                            firstNames[fname][1] += 1
                print(file)
    return firstNames

# open the directory with the raw data
path = '../data/rawData/'
out = readNames(path)
writer = csv.writer(open('../data/brazilNamesSexCounts.csv', 'w', newline = '', encoding='ISO-8859-1'))

writer.writerow(['firstName', 'total', 'female', 'male'])

for k, v in out.items():
    writer.writerow([k] + [num for num in v])
