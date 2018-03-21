#!/usr/bin/env python3

import csv


def checkIntersection():
    matched = []
    count = 0
    for row in districtInfo:
        for irns in irnLookups.values():
            if int(float(row[1])) in irns:
                matched.append(int(float(row[1])))
                break


    for row in districtInfo:
        if int(float(row[1])) not in matched:
            print('Did not match', row[1], 'to irnLookups dictionary')


    print('Matched', len(matched), 'out of', len(districtInfo), 'schools from districtInfo to irnLookups')


# grad.csv is what helps us map IRN's to County names
# Build IRN dictionary: (String)county name: (List)IRN
irnLookups = {}
with open('grad.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        # Row 2 is district name
        # Row 0 is IRN
        if row[2] not in irnLookups:
            if row[2] != 'County':
                irnLookups[row[2]] = [int(row[0])]
        else:
            temp = irnLookups.get(row[2])
            temp.append(int(row[0]))
            irnLookups[row[2]] = temp


# mort.csv is all of the mortality data and is categorized by 
# county name, which is why we had to relate IRN's to county
# names.
# Build mortality
mortality = []
line = 0
with open('mort.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        # Ohio lines are between 2081 and 2170
        if line > 2081 and line < 2170:
            temp = row[0].split(",")
            mortality.append(row)

        # If we get to line 2170, we're done
        if line >= 2170:
            break

        line += 1


# Begin parsing district.csv, which contains various information
# on schools by district
districtInfo = []
with open('district.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        districtInfo.append(row)


# Trim off first two rows which are column names and empty space
districtInfo = districtInfo[2:]


# Validate intersection between two data sets
checkIntersection()



