#!/usr/bin/env: python3

'''

Source: https://stackoverflow.com/questions/20105118/convert-xlsx-to-csv-correctly-using-python

'''

import xlrd
import csv
import argparse
import os.path

def csv_from_excel():
    wb = xlrd.open_workbook('excel.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('your_csv_file.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
#csv_from_excel()

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
