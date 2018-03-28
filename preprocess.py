#!/usr/bin/env python3

#
# CRI: Percentage spent on classroom instruction
# NCR: Percentage spent on non-classroom
# ADM: Average Daily Membership
#

import csv
import pandas as pd
import numpy as np

#
# Builds a list of school information that is in the intersection
# of grad and expanded csv's
#
# TODO: Match first column to irnLookups to get an intersection of data
def getIntersection(temp, irnLookups):
    matched = pd.DataFrame(columns=['IRN','Local Education Agency Name', 'Org Type','Weighted ADM','Operating Expenditures','CRI%','NCR%','Instruction', 'Pupil Support', 'Instr Staff Sup', 'CRI - Classroom Instr', 'Gen Admin', 'School Admin', 'Oper & Maint', 'Pupil Transp', 'Other Support', 'Food Service', 'NCR -Nonclassroom', 'Enterprise', 'Other Elem-Sec', 'Community Service', 'Adult Ed', 'Other Non Elem-Sec', 'Construction', 'Land & Structures', 'Instr Equipment', 'Other Equipment', 'Debt & Interest', 'Non-Operating', 'Operating EPEP'])
	
    for i in range(temp.shape[0]):
        for irns in irnLookups.values():
            if int(temp.iat[i, 0]) in irns:
                matched = matched.append(temp.iloc[i], ignore_index=True)

    return matched        

#
# Builds a list of school information that does not match 
# irnLookup table
#
# def getComplement(matched):
#     complement = []
#     for row in districtInfo:
#         if int(float(row[0])) not in matched:
#             complement.append(row)

#     print("Found", len(complement), "schools that are not in irnLookups")
#     return complement


# # Print list of matching IRNs
# def printLookups(irn_list):
#     for i in irnLookups:
#         print (i, irnLookups.get(i))


def main():
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


    # Parse expanded.csv, which contains various information
    # on schools by district. However, we need to abstract IRN's by
    # county so we will take the intersection of district info and
    # irnLookups.
    districtInfo = pd.read_csv("expanded.csv", sep=',', quotechar='"')
    districtInfo = getIntersection(districtInfo, irnLookups)

    # mort.csv is all of the mortality data and is categorized by 
    # county name, which is why we had to relate IRN's to county
    # names.
    # Would like to prepend the first row so we can have names of columns
    allMortality = pd.read_csv("mort.csv", sep=',', quotechar='"')
    ohioMortality = allMortality.iloc[2081:2169, :]


    # At this point, we have a list of mortality rate data and a list
    # of school district financial expenditures. We've matched IRN's 
    # to county names to better zero in on a local area.


main()