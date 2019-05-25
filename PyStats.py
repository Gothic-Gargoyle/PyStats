#!/usr/bin/env python3

# Name: PyStat
# Version: 0.1
# Description: Statistical functions in Python in order to learn python, woo!
# License: none yet

# Read files!
# readCSVFile

import csv

# TODO: generalize readFile (CSV, JSON, ETC)
def readCSVFile(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {",".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')

readCSVFile("test.txt")
