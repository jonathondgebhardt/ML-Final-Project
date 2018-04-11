#!/usr/bin/env: python3

# Source: https://stackoverflow.com/questions/20105118/convert-xlsx-to-csv-correctly-using-python


# TODO: Don't make a sheet name necessary. If none is provided, assume there's only one sheet.
# TODO: Handle errors with sheet name gracefully
# ValueError: Sheet name is not in list
# XLRDError: No sheet named ... 


import xlrd
import csv
import argparse
import os.path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="name of excel workbook to be converted")
    parser.add_argument("sheet_name", help="name of excel workbook sheet to be converted")
    parser.add_argument("output_file_name", help="name of output file")
    args = parser.parse_args()



    if os.path.isfile(args.file_name):
        wb = xlrd.open_workbook(args.file_name)
        sh = wb.sheet_by_name(args.sheet_name)
        your_csv_file = open(args.output_file_name, 'w')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        your_csv_file.close()

    else:
        print("Error: File " + args.file_name + " does not exist")

main()