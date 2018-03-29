#!/usr/bin/env python3

#
# TODO: Normalize data. Operating expenditures blows everything out of proportion
# when everything is plotted.
#


#
# CRI: Percentage spent on classroom instruction
# NCR: Percentage spent on non-classroom
# ADM: Average Daily Membership
#

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

columnNames = [
        'IRN','Local Education Agency Name', 'Org Type','Weighted ADM','Operating Expenditures','CRI%',
        'NCR%','Instruction', 'Pupil Support', 'Instr Staff Sup', 'CRI - Classroom Instr', 'Gen Admin',
        'School Admin', 'Oper & Maint', 'Pupil Transp', 'Other Support', 'Food Service',
        'NCR -Nonclassroom', 'Enterprise', 'Other Elem-Sec', 'Community Service', 'Adult Ed',
        'Other Non Elem-Sec', 'Construction', 'Land & Structures', 'Instr Equipment', 'Other Equipment',
        'Debt & Interest', 'Non-Operating', 'Operating EPEP'
        ]

#
# Builds a list of school information that is in the intersection
# of grad and expanded csv's
#
# When creating a new dataframe object to work with, we are getting an additional 
# 'Instr Staff Sup' column (we have duplicates of this column). The first appearance
# of this column has value NaN, the second appearance as the actual value.
#
def getIntersection(universe, irnLookups):
    # Create an empty data frame object with these labels as columns
    matched = pd.DataFrame(columns=columnNames)
	
    # Iterate entire original dataframe object searching for IRN's that we know of.
    # If found, add to new dataframe.
    for i in range(universe.shape[0]):
        for irns in irnLookups.values():
            if int(universe.iat[i, 0]) in irns:
                matched = matched.append(universe.iloc[i], ignore_index=True)

    return matched        

#
# Builds a list of school information that does not match 
# irnLookup table
#
def getComplement(universe, irnLookups):
    # Create an empty data frame object with these labels as columns
    complement = pd.DataFrame(columns=columnNames)
	
    # Iterate entire original dataframe object searching for IRN's that we know of.
    # If not found, add to new dataframe.
    found = False
    for i in range(universe.shape[0]):
        for irns in irnLookups.values():
            if int(universe.iat[i, 0]) in irns:
                found = True
                break
            
        if not found:
            complement = complement.append(universe.iloc[i], ignore_index=True)
            found = False

    return complement


# # Print list of matching IRNs
# def printLookups(irn_list):
#     for i in irnLookups:
#         print (i, irnLookups.get(i))


def main():
    # grad.csv is what helps us map IRN's to County names. We will
    # use it for cross-referencing
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

    totalSchoolsInLookup = 0
    for irns in irnLookups.values():
        totalSchoolsInLookup += len(irns)

    print('Schools in lookup table:', totalSchoolsInLookup)


    # Parse expanded.csv, which contains various information
    # on schools by district. However, we need to abstract IRN's by
    # county so we will take the intersection of district info and
    # irnLookups.
    ohioSchools = pd.read_csv("expanded.csv", sep=',', quotechar='"')
    ohioSchoolsIntersection = pd.read_csv("expanded_intersection.csv", sep=',', quotechar='"')
    ohioSchoolsComplement = pd.read_csv("expanded_complement.csv", sep=',', quotechar='"')

    print('Total schools in dataset:', ohioSchools.shape[0])
    print('Total schools in intersection:', ohioSchoolsIntersection.shape[0])
    print('Total schools in complement:', ohioSchoolsComplement.shape[0])

    missing = ohioSchools.shape[0] - (ohioSchoolsComplement.shape[0] + ohioSchoolsIntersection.shape[0])
    print('Schools not accounted for', missing)


    # mort.csv is taken from an excel workbook that contains mortality
    # rates of counties by mortality type. We've selected the "Mental and 
    # substance abuse" sheet because it applies directly to what we're looking
    # for. We could potentially look at other sheets.
    #
    # The first column is county name, second column is FIPS number, every 
    # column except for the last is the mortality rate of that year 
    # (1980 - 2014 by increments of 5 years), and the last column is the 
    # overall change in mortality throughout the years.
    #
    # Build mortality, but only get mortality info for Ohio (Rows 2081 - 2168)
    allMortality = pd.read_csv("mort.csv", sep=',', quotechar='"')
    ohioMortality = allMortality.iloc[2081:2169, :]


    # At this point, we have a list of mortality rate data and a list
    # of school district financial expenditures. We've matched IRN's 
    # to county names to better zero in on a local area.

    ohioSchoolsIntersection.hist()
    plt.show()

    ohioSchoolsIntersection.boxplot()
    plt.show()




main()