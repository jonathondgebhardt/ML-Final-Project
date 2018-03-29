import csv

# Build IRN look up list. We only need a list of all unique IRNs in this case.
irns = []
with open('grad.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        #reader.next()
        for row in reader:
            if row[2] not in irns and row[2] != 'County':
                irns.append(int(row[0]))
          
          
# Build a list of intersection and complement IRNs in order to decrease
# amount of time building lists in preprocess.py
intersection, complement = [], []
with open('expanded.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # Get column labels and put them in lists first
    d_reader = csv.DictReader(csvfile)
    headers = d_reader.fieldnames
    intersection.append(headers)
    complement.append(headers)

    # Iterate list of schools. If IRN is in lookup table, add to intersection.
    # Otherwise, add to complement.
    for row in reader:
        if row[0] != 'IRN' and int(row[0]) in irns:
            intersection.append(row)
        else:
            complement.append(row)


# Write lists out to files
with open('expanded_intersection.csv', 'w', newline='') as csvfile:
    out = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in intersection:
        out.writerow(row)
    
with open('expanded_complement.csv', 'w', newline='') as csvfile:
    out = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in complement:
        out.writerow(row)