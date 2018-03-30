import csv

# TODO: Merge trim and preprocess script

# Build IRN look up list so that we can correlate County names to school
# districts. This will be useful in building our final data set.
irnLookups = {}
with open('grad.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        
        # Column 2 is county name. We're skipping the first row and looking
        # at the IRNs. If the IRN isn't already in the lookup table, add
        # the IRN as a key and the county as a value. 
        if row[2] != 'County' and int(row[0]) not in irnLookups.keys():
            irnLookups[int(row[0])] = row[2]


# Build a list of intersection and complement IRNs in order to decrease
# amount of time building lists in preprocess.py.
intersection, complement = [], []
with open('expanded.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # Get column labels and put them in lists first
    d_reader = csv.DictReader(csvfile)
    headers = d_reader.fieldnames
    complement.append(headers)
    headers.append('County Name')
    headers.append('County Mortality Rate')
    intersection.append(headers)

    # Iterate list of schools. If IRN is in lookup table, add to intersection.
    # Otherwise, add to complement.
    for row in reader:
        if row[0] != 'IRN' and int(row[0]) in irnLookups.keys():
            intersection.append(row)
        else:
            complement.append(row)


# Get a list of all mortality rates
allMortalityRates = []
with open('mort.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    for row in reader:
        allMortalityRates.append(row)

# We only want ones that are relevant, meaning mortality rates for Ohio
intersectMortalityRates = allMortalityRates[2081:2169]


# Write out intersection list to file
with open('expanded_intersection.csv', 'w', newline='') as csvfile:
    out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for row in intersection:
        # Get county name from irnLookups so that we can append to
        # correct row. Again, we want to skip the first row to avoid
        # issues with casting row[0].
        if row[0] != 'IRN':    
            countyName = irnLookups.get(int(row[0]))
            #mortalityRate = 'None'

            # Get mortality rate for that county from intersectMortalityRates
            # Column 9 in mort.csv is mortality rate for 2014
            # Column 0 in mort.csv is county name
            for county in intersectMortalityRates:
                if countyName in county[0]:
                    mortalityRate = county[9]

            # Append to row
            row.append(countyName)
            row.append(mortalityRate)

        # Finally, write to file
        out.writerow(row)
    

# Write out complement list to file. We don't have county names for these IRN's
# so we're ignoring them for now.
with open('expanded_complement.csv', 'w', newline='') as csvfile:
    out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in complement:
        out.writerow(row)


