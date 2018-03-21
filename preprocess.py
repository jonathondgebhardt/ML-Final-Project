#!/usr/bin/env python3

import csv

irnLookups = {}
irnCount = 0


# grad.csv is what helps us map IRN's to County names
# Build IRN dictionary: (String)county name: (List)IRN
with open('grad.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        # Row 2 is district name
        # Row 0 is IRN
        print(row[0])
        if row[2] not in irnLookups:
            if row[2] != 'County':
                irnLookups[row[2]] = [row[0]]
        else:
            temp = irnLookups.get(row[2])
            temp.append(row[0])
            irnLookups[row[2]] = temp
         
        irnCount += 1



print('\nTotal schools in grad.csv:', irnCount)
print('Total counties in grad.csv:', len(irnLookups))


# TODO: Get all columns from this data set
# mort.csv is all of the mortality data and is categorized by 
# county name, which is why we had to relate IRN's to county
# names.
# Build mortality
mortCounties = []
line = 0
with open('mort.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if line > 2081 and line < 2170:
            temp = row[0].split(",")
            mortCounties.append(temp[0].replace(' County', ''))
        line += 1

print('Total counties in mort.csv:', len(mortCounties))

mostSchools = ""
count = 0
for k in irnLookups:
    if len(irnLookups[k]) > count:
        count = len(irnLookups[k])
        mostSchools = k

print(mostSchools, 'has most schools at', count)


# Begin parsing district.csv, which contains various information
# on schools by district
districtInfo = []
line = 0
with open('district.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        districtInfo.append(row)

districtInfo = districtInfo[2:]

count = 0
for row in districtInfo:
    for irns in irnLookups.values():
        print(str(irns))
        k = input()
        if str(int(float(row[1]))) in irns:
            count += 1
            break

print('Matched', count, 'schools from districtInfo to irnLookups')
