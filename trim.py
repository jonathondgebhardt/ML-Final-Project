import csv

# Build IRN look up list. We only need a list of all unique IRNs in this case.
# grad.csv is what helps us map IRN's to County names. We will
# use it for cross-referencing
irns = []
irnLookups = {}
with open('grad.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row[2] not in irns and row[2] != 'County':
            irns.append(int(row[0]))

    csvfile.seek(0)

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


# Build a list of intersection and complement IRNs in order to decrease
# amount of time building lists in preprocess.py
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
        if row[0] != 'IRN' and int(row[0]) in irns:
            intersection.append(row)
        else:
            complement.append(row)


allMortalityRates = []
# TODO: Put mortality rates into school district data set
# Write lists out to files
# Read mortality rates, append each county's mortality rate to the last column
with open('mort.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    for row in reader:
        allMortalityRates.append(row)

intersectMortalityRates = allMortalityRates[2081:2169]


with open('expanded_intersection.csv', 'w', newline='') as csvfile:
    out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in intersection:
        for county in irnLookups:
            if row[0] in irnLookups.get(county):
                

        out.writerow(row)
    
with open('expanded_complement.csv', 'w', newline='') as csvfile:
    out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in complement:
        out.writerow(row)



