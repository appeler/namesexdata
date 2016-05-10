# Author: Luke Sonnet
# Purpose: Takes raw candidate from the 2010 elections in Sweden and counts firstNames
#          names and genders
#
# Python v: 3.5.4

from os import walk
import csv

firstNames = {}

def readNames(dir):
    """Loads the files, records the names, and counts the sexes"""
    for root, dirs, files in walk(path):
        for file in files:
            if file.endswith('.skv'):
                f = csv.reader(open(root + '/' + file, 'r', encoding='ISO-8859-1'), delimiter=';')
                for n, i in enumerate(f):
                    if n != 0:

                        m = len(i)
                        # Get first name only as everything preceding first space
                        fname = i[m-4].split(" ")[0]

                        # From brazil, may be unnecessary in Sweden, can't hurt?
                        fname = fname.replace('`', '')
                        fname = fname.replace(',', '')
                        fname = fname.replace(']', '')

                        # if name exists, add to it, else create name
                        if not fname in firstNames.keys():
                            firstNames[fname] = [1, 0, 0]
                        else:
                            firstNames[fname][0] += 1
                        # males are 'M', females are 'K'
                        if i[m-2] == 'M':
                            firstNames[fname][2] += 1
                        elif i[m-2] == 'K':
                            firstNames[fname][1] += 1
                print(file)
    return firstNames

# open the directory with the raw data
path = 'data-raw/'
out = readNames(path)
writer = csv.writer(open('swedenNamesSex.csv', 'w', newline = '', encoding='ISO-8859-1'))

writer.writerow(['firstName', 'total', 'female', 'male', 'prFemale'])

for k, v in out.items():

    # There is no missing sex data so we can calculate pr female just as female/total
    prFemale = v[1]/v[0]
    writer.writerow([k] + [num for num in v] + [prFemale])
