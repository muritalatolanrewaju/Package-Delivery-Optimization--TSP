# Name: Muritala Olanrewaju
# Student ID: 010882332

class Distance:
    # Class to represent a distance table

    # Constructor
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.distance_table = []
        self.labels = self.extract_labels()

    # Extracts labels from raw data
    def extract_labels(self):
        return [label for label in self.raw_data.pop(0) if label]

    # Cleans and sorts data into a structured list
    def clean_and_sort_data(self):
        for row in self.raw_data:
            key = row[0]
            sub_key_val_pairs = [[label, value] for label, value in zip(self.labels, row[1:])]
            self.distance_table.append([key, sub_key_val_pairs])
        return self.distance_table

    # Retrieves the labels used in the distance table
    def get_labels(self):
        return self.labels
