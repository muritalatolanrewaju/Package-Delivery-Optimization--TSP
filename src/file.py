# Name: Muritala Olanrewaju
# Student ID: 010882332

import csv

from hash_table import SelfAdjustingHash
from package import Package


class File:
    # A file that can be parsed.

    # Initialization
    def __init__(self, file):
        self.file = file
        self.row_count = self.get_row_count()

    # Get the number of rows in the file
    def get_row_count(self):
        return sum(1 for _ in open(self.file, 'r'))

    # Parse the package data
    def parse_package_data(self):
        hash_table = SelfAdjustingHash(self.row_count)
        with open(self.file, mode='r', encoding='utf-8-sig') as csv_data:
            data = csv.reader(csv_data, delimiter=',')
            for row in data:
                package = Package(*row[:7], 'At HUB', row[7])
                hash_table.add(row[0], package)
        return hash_table

    # Parse the distance data from CSV and return a list
    def parse_distance_data(self):
        raw_data = []
        with open(self.file, mode='r', encoding='utf-8-sig') as csv_data:
            data = csv.reader(csv_data, delimiter=',')
            for row in data:
                if row[0] == '5383 S 900 East #104':
                    row[0] = '5383 South 900 East #104'
                raw_data.append(row)
        return raw_data
