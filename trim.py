import csv

input_variables = [
    'Attendance 2012-13', 'Attendance 2010-11', 
    'Other Elem-Sec', 'Attendance 2011-12', 
    'District Class 2 Effective Millage Incl JVS FY14', 
    'District Percent of Students In Poverty FY13', 
    'District Local Revenue As % Of Total FY13', 
    'Performance Index Score 2012-13', 
    'District Average Income TY11', 'Adult Ed', 
    'District Median Income TY11'
    ]

def get_index(column_name, arr):
    # Iterate through headers of data set looking for column 
    # that contains IRNs
    headers = arr[0]
    print(headers)
    for i in range(len(headers)):
        if column_name in headers[i]:
            return i


def get_headers(file_name):
    # Get the column names from the data set so that we can append 
    # them to the new data set
    d_reader = csv.DictReader(csvfile)
    headers = d_reader.fieldnames

    return headers

def get_file_contents(file):
    contents = []
    reader = csv.reader(file, delimiter=',', quotechar='"')

    for row in reader:
        contents.append(row)

    return contents

# We will base our merge on the lrc data set since it contains both 
# counties and LRCs
with open('lrc.csv', newline='') as csvfile:
    lrc_headers = get_headers(csvfile)
    lrc_contents = get_file_contents(csvfile)


#expanded_contents = []
with open('expanded.csv', newline='') as csvfile:
    expanded_headers = get_headers(csvfile)
    expanded_contents = get_file_contents(csvfile)
    

with open('cupp.csv', newline='') as csvfile:
    cupp_headers = get_headers(csvfile)
    cupp_contents = get_file_contents(csvfile)


# Now that we have the contents of all the files, we need to get
# the appropriate column for IRNs

# Before we can merge, we need to get he headers from all datasets
all_headers = []
for header in lrc_headers:
    all_headers.append(header)

for header in expanded_headers:
    all_headers.append(header)

for header in cupp_headers:
    all_headers.append(header)

print(all_headers)
lrc_irn_column = get_index('IRN', lrc_headers)
cupp_irn_column = get_index('IRN', cupp_headers)
expanded_irn_column = get_index('IRN', expanded_headers)


collosus = []
# collosus.append(all_headers)
for lrc_row in lrc_contents[1:len(lrc_contents)-2]:
    # Get current row IRN
    lrc_row_irn = int(float(lrc_row[lrc_irn_column]))

    # Iterate through other data sets
    for expanded_row in expanded_contents[1:]:
        if int(float(expanded_row[expanded_irn_column])) == lrc_row_irn:
            for entry in expanded_row:
                lrc_row.append(entry)
            break

    for cupp_row in cupp_contents[2:]:
        if int(float(cupp_row[cupp_irn_column])) == lrc_row_irn:
            for entry in cupp_row:
                lrc_row.append(entry)
            break

    collosus.append(lrc_row)

print(len(collosus))
print(len(collosus[0]))

# # Build a list of intersection and complement IRNs in order to decrease
# # amount of time building lists in preprocess.py.
# expandedHeaders = []
# with open('expanded.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     d_reader = csv.DictReader(csvfile)
#     headers = d_reader.fieldnames

# cuppHeaders = []
# with open('cupp.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     d_reader = csv.DictReader(csvfile)
#     cuppHeaders = d_reader.fieldnames

# lrcHeaders = []
# with open('lrc.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     d_reader = csv.DictReader(csvfile)
#     lrcHeaders = d_reader.fieldnames

# intersect = []
# complement = []
# for header in expandedHeaders:
#     if header in universe:
#         intersect.append(header)

# for header in cuppHeaders:
#     if header in universe:
#         intersect.append(header)

# for header in lrcHeaders:
#     headerStripped = header.strip()
#     if headerStripped in universe:
#         intersect.append(headerStripped)
#     else:
#         complement.append(headerStripped)

# print(len(lrcHeaders))
# print(len(complement))

# for header in complement:
#     print('"', header, '"')
#     k = input()


# print('universe length:', len(universe))
# print('intersection length:', len(intersect))
# print('complement length:', len(universe) - len(intersect))

# print('Universal headers')
# for header in bigHeaders:
#     print('\t', header)

# print('\nThe following are in the intersection')
# for header in intersectionHeaders:
#     print('\t', header)

#     # Get column labels and put them in lists first
#     d_reader = csv.DictReader(csvfile)
#     headers = d_reader.fieldnames
#     complement.append(headers)
#     headers.append('County Name')
#     headers.append('County Mortality Rate')
#     headers.append('Letter Grade')
#     headers.append('A/Not A')
#     intersection.append(headers)

#     # Iterate list of schools. If IRN is in lookup table, add to intersection.
#     # Otherwise, add to complement.
#     for row in reader:
#         if row[0] != 'IRN' and int(row[0]) in irnLookups.keys():
#             intersection.append(row)
#         else:
#             complement.append(row)


# # Get a list of all mortality rates
# allMortalityRates = []
# with open('mort.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='"')

#     for row in reader:
#         allMortalityRates.append(row)

# # We only want ones that are relevant, meaning mortality rates for Ohio
# intersectMortalityRates = allMortalityRates[2081:2169]


# # Write out intersection list to file
# letterEncode = {'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1, 'F' : 0}
# with open('expanded_intersection.csv', 'w', newline='') as csvfile:
#     out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
#     for row in intersection:
#         # Get county name from irnLookups so that we can append to
#         # correct row. Again, we want to skip the first row to avoid
#         # issues with casting row[0].
#         letter = '!'

#         if row[0] != 'IRN':    
#             countyName = irnLookups.get(int(row[0]))

#             # Get letter grade of four year graduation rate from grad.csv. This is
#             # a potential output variable. 
#             for school in gradRows:
#                 # We're looking for a matching IRN here. Once we've found it, get
#                 # the letter grade and whether it's A or not.
#                 if int(row[0]) == int(school[0]):
#                     letter = letterEncode.get(school[9])

#                     if letter:
#                         isA = int(letter / 4)

#                     break

#             # Get mortality rate for that county from intersectMortalityRates
#             # Column 9 in mort.csv is mortality rate for 2014
#             # Column 0 in mort.csv is county name
#             for county in intersectMortalityRates:
#                 if countyName in county[0]:
#                     mortalityRate = county[9]
#                     break

#             # Append to row
#             row.append(countyName)
#             row.append(mortalityRate)
#             row.append(letter)
#             row.append(isA)

#         # Finally, write to file
#         if letter:
#             out.writerow(row)   
    

# # Write out complement list to file. We don't have county names for these IRN's
# # so we're ignoring them for now.
# with open('expanded_complement.csv', 'w', newline='') as csvfile:
#     out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     for row in complement:
#         out.writerow(row)


# # Now that we have the combined dataset, trim off rows that we don't want
# # Or rather, specify the columns that we want to keep and write to csv file
# with open("expanded_intersection.csv","r") as source:
#     rdr= csv.reader( source )
#     with open("expanded_intersection_trimmed.csv","w") as result:
#         wtr= csv.writer( result )
#         for r in rdr:
#             # Columns we want to keep
#             wtr.writerow( (r[0], r[1], r[4], r[5], r[6], r[7], r[8], r[9], r[10], 
#             r[11], r[12], r[13], r[14], r[15], r[17], r[19], r[22], r[28], r[29], 
#             r[30], r[31], r[32], r[33]))

    