
class CoefMatrix():
    def __init__(self):
        self.data = []
        self.rows = []
        self.cols = []

    def add_entry(self, row, col, data_value):
        self.data.append(data_value)
        self.rows.append(row)
        self.cols.append(col)

    def add_entries(self, entry_list):
        for ent in entry_list:
            self.add_entry(ent[0], ent[1], ent[2])