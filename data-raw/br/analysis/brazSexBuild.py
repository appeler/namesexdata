# Author: Luke Sonnet
# Purpose: Takes raw candidate from 1998-2014 in Brazil, strips out the first
#          word in the name field, records the sex, and saves it in a large csv
#          file. The name is always field 10, but the sex column moves: general
#          election years carry CPF and so sit one column right of municipal
#          years, and 576 malformed 2008 rows are shifted one column left. So
#          sex is read from its label, not its position.
#
# Python v: 3.5.4

import csv
from os import walk

firstNames = {}
SEXES = ("MASCULINO", "FEMININO")


def readNames(dir):
    """Loads the files, records the names, and counts the sexes"""
    for root, dirs, files in walk(path):
        for file in files:
            if file.endswith((".txt", ".csv")):
                f = csv.reader(
                    open(root + "/" + file, "r", encoding="ISO-8859-1"), delimiter=";"
                )
                for i in f:
                    # Only five files open with a column-name header
                    if not i[2].isdigit():
                        continue
                    # Get first name only as everything preceding first space
                    fname = i[10].split(" ")[0]

                    fname = fname.replace("`", "")
                    fname = fname.replace(",", "")
                    fname = fname.replace("]", "")

                    # if name exists, add to it, else create name
                    if fname not in firstNames:
                        firstNames[fname] = [1, 0, 0]
                    else:
                        firstNames[fname][0] += 1
                    # First match is the sex column; two 2012 rows repeat
                    # MASCULINO later, as the birth municipality
                    sex = next((v for v in i[20:] if v in SEXES), None)
                    if sex == "MASCULINO":
                        firstNames[fname][2] += 1
                    elif sex == "FEMININO":
                        firstNames[fname][1] += 1
                print(file)
    return firstNames


# open the directory with the raw data
path = "../data/rawData/"
out = readNames(path)
writer = csv.writer(
    open("../data/brazilNamesSexCounts.csv", "w", newline="", encoding="ISO-8859-1")
)

writer.writerow(["firstName", "total", "female", "male"])

for k, v in out.items():
    writer.writerow([k] + [num for num in v])
