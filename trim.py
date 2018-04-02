import csv

# TODO: Merge trim and preprocess script

# Build IRN look up list so that we can correlate County names to school
# districts. This will be useful in building our final data set.
irnLookups = {}
gradRows = []
with open('grad.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        
        # Column 2 is county name. We're skipping the first row and looking
        # at the IRNs. If the IRN isn't already in the lookup table, add
        # the IRN as a key and the county as a value. 
        if row[2] != 'County' and int(row[0]) not in irnLookups.keys():
            irnLookups[int(row[0])] = row[2]
            gradRows.append(row)


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
    headers.append('Letter Grade')
    headers.append('A/Not A')
    intersection.append(headers)

    # Iterate list of schools. If IRN is in lookup table, add to intersection.
    # Otherwise, add to complement.
    for row in reader:
        if row[0] != 'IRN' and int(row[0]) in irnLookups.keys():
            intersection.append(row)
        else:
            complement.append(row)


# Get a list of all mortality rates
# allMortalityRates = []
# with open('mort.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='"')

#     for row in reader:
#         allMortalityRates.append(row)

# We only want ones that are relevant, meaning mortality rates for Ohio
#intersectMortalityRates = allMortalityRates[2081:2169]


letterEncode = {'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1, 'F' : 0}
# Write out intersection list to file
with open('expanded_intersection.csv', 'w', newline='') as csvfile:
    out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for row in intersection:
        # Get county name from irnLookups so that we can append to
        # correct row. Again, we want to skip the first row to avoid
        # issues with casting row[0].
        letter = 'Z'
        isA = 1
        if row[0] != 'IRN':    
            countyName = irnLookups.get(int(row[0]))
            #mortalityRate = 'None'

            # Get mortality rate for that county from intersectMortalityRates
            # Column 9 in mort.csv is mortality rate for 2014
            # Column 0 in mort.csv is county name
            for school in gradRows:
                if int(row[0]) == int(school[0]):
                    letter = letterEncode.get(school[9])
                    if school[9] != 'A':
                        isA = 0
                    

            # Append to row
            row.append(countyName)
            row.append(letter)
            row.append(isA)

        # Finally, write to file
        out.writerow(row)   
    

# Write out complement list to file. We don't have county names for these IRN's
# so we're ignoring them for now.
with open('expanded_complement.csv', 'w', newline='') as csvfile:
    out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in complement:
        out.writerow(row)


# Now that we have the combined dataset, trim off rows that we don't want
# Or rather, specify the columns that we want to keep and write to csv file
with open("expanded_intersection.csv","r") as source:
    rdr= csv.reader( source )
    with open("expanded_intersection_trimmed.csv","w") as result:
        wtr= csv.writer( result )
        for r in rdr:
            # Columns we want to keep
            wtr.writerow( (r[0], r[1], r[4], r[5], r[6], r[7], r[8], r[9], r[10], 
            r[11], r[12], r[13], r[14], r[15], r[17], r[19], r[22], r[28], r[29], 
            r[30], r[31], r[32]))

    