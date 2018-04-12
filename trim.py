import csv

input_variables = [
    'Attendance 2012-13', 'Attendance 2010-11', 
    'Other Elem-Sec', 'Attendance 2011-12', 
    'District Class 2 Effective Millage Incl JVS FY14', 
    'District Percent Of Students In Poverty FY13', 
    'District Local Revenue As % Of Total FY13', 
    'Performance Index Score 2012-13', 
    'District Average Income TY11', 'Adult Ed', 
    'District Median Income TY11'
    ]

target_variables = [
    'County Mortality Rate', 'Mortality Level'
    ]

def get_index(column_name, headers):
    # Iterate through headers of data set looking for column 
    # that contains IRNs

    for i in range(len(headers)):
        if column_name in headers[i]:
            return i

def get_headers(file_name):
    # Get the column names from the data set so that we can append 
    # them to the new data set
    d_reader = csv.DictReader(csvfile)
    headers = d_reader.fieldnames

    return headers

# Read file, append each line to a list, and return list
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

with open('mort.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    count = 0
    ohio_mortality_rates = []
    for row in reader:
        
        if count == 2170:
            break

        if count > 2081:
            county = row[0].split('County, ')[0]
            rate = row[9].split(' ')[0]
            
            #0-12, 12-24, 24+
            if float(rate) < 12:
                mortality_category = 'low'
            elif float(rate) < 24:
                mortality_category = 'med'
            else:
                mortality_category = 'high'

            ohio_mortality_rates.append([county, rate, mortality_category])
        
        count += 1

# Before we can merge, we need to get and merge headers from each data set
all_headers = []
for header in lrc_headers:
    all_headers.append(header)

for header in expanded_headers:
    all_headers.append(header)

for header in cupp_headers:
    all_headers.append(header)

# We need to get the IRN row so that we can match each row up
lrc_irn_column = get_index('IRN', lrc_headers)
cupp_irn_column = get_index('IRN', cupp_headers)
expanded_irn_column = get_index('IRN', expanded_headers)

# Now we can merge all the datasets. We want to skip the first row and stop 
# early to avoid weird casting issues.
collosus = []
collosus.append(all_headers)
for lrc_row in lrc_contents[1:len(lrc_contents)-2]:
    # Get current row IRN
    lrc_row_irn = int(float(lrc_row[lrc_irn_column]))

    # Iterate through other data sets looking for current row IRN
    # Once found, append each entry to row
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

    # Now append row to big data set
    collosus.append(lrc_row)

# Get indices of input variables
input_variables_indices = []

for variable in input_variables:
    for i in range(len(all_headers)):
        if all_headers[i] == variable:
            input_variables_indices.append(i)
            break

# Build list of headers
trimmed_dataset_headers = ['IRN', 'County']
for input_variable in input_variables:
    trimmed_dataset_headers.append(input_variable)

trimmed_dataset_headers.append('County Mortality Rate')
trimmed_dataset_headers.append('County Mortality Category')

trimmed_dataset = []
trimmed_dataset.append(trimmed_dataset_headers)

# Iterate big data set adding only columns of input variables
for row in collosus[1:]:
    # Use a try catch to omit rows that are missing information
    try:
        row_irn = row[0]
        row_county = row[2]
        
        temp = []
        temp.append(row_irn)
        temp.append(row_county)

        # Append all target variables
        for index in input_variables_indices:
            temp.append(row[index])

        # Append mortality information
        for county in ohio_mortality_rates:
            if row_county in county[0]:
                temp.append(county[1]) # Mortality rate percentage
                temp.append(county[2]) # Predifined mortality rate category

        trimmed_dataset.append(temp)

    except IndexError:
        continue

# Write out trimmed dataset to file
with open('trimmed.csv', 'w', newline='') as csvfile:
    out = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in trimmed_dataset:
        out.writerow(row)
