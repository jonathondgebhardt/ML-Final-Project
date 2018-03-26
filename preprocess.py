#!/usr/bin/env python3

#
# CRI: Percentage spent on classroom instruction
# NCR: Percentage spent on non-classroom
# ADM: Average Daily Membership
#

import csv


#
# Builds a list of school information that is in the intersection
# of grad and expanded csv's
#
def getIntersection():
    matched = []
    count = 0
    for row in districtInfo:
        for irns in irnLookups.values():
            if int(float(row[0])) in irns:
                matched.append(int(float(row[0])))
                break

    return matched


#
# Builds a list of school information that does not match 
# irnLookup table
#
def getComplement(matched):
    complement = []
    for row in districtInfo:
        if int(float(row[0])) not in matched:
            complement.append(row)

    print("Found", len(complement), "schools that are not in irnLookups")
    return complement


# Print list of matching IRNs
def printLookups(irn_list):
    for i in irnLookups:
        print (i, irnLookups.get(i))


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
with open('expanded.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        districtInfo.append(row)


# Trim off first row which is column names 
districtInfo = districtInfo[1:]


# Validate intersection between two data sets
schoolIntersection = getIntersection()
getComplement(schoolIntersection)


# At this point, we have a list of mortality rate data and a list
# of school district financial expenditures. We've matched IRN's 
# to county names to better zero in on a local area.


