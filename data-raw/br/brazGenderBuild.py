# File: brazGenderBuild.py
#
# Purpose: Takes candidate data from the 2012 and 2008 municipal elections to 
#          calculate the number of people with that name belonging to either #          the female or male genders
#
# Authors: Luke Sonnet (Feb 2015)
#
# History:
#    10 Feb 2015: Initial code
#
# Python v: 2.7.8

import unicodecsv
from os import listdir

firstNames = {}

def readFile(dir):
    """Loads the files, records the names, and counts the genders"""
    files = listdir(dir)
    for file in files:
        f = unicodecsv.reader(open(dir + '/' + file, 'rb'), encoding='ISO-8859-1', delimiter=';')
        for n, i in enumerate(f):
            if n != 0:
            
                # Get first name only as everything preceding first space
                fname = i[10].split(" ")[0]
                
                # if name exists, add to it, else create name
                if not fname in firstNames.keys():
                    firstNames[fname] = [1, 0, 0]
                else:
                    firstNames[fname][0] += 1
                    
                # men are '2', women are '4'
                if i[28] == '2':
                    firstNames[fname][2] += 1
                elif i[28] == '4':
                    firstNames[fname][1] += 1
        print file
    return firstNames
            
# open the directory with the raw data
dir = '../../../../Documents/cand_data'
out = readFile(dir)
writer = unicodecsv.writer(open("brazilNamesGenderCounts.csv",'wb'), encoding='ISO-8859-1')

writer.writerow(['firstName', 'total', 'female', 'male'])

for k, v in out.iteritems():
    writer.writerow([k] + [num for num in v])
