import csv
import os

class CsvReader():

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.file = None
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        if self.filename is None or not os.path.isfile(self.filename):
            print("File not found")
            return None
        try:
            ref_size = -1
            self.file = open(self.filename, 'r')
            datas = csv.reader(self.file, delimiter=self.sep, skipinitialspace=True)
            for row in datas:
                if ref_size == -1:
                    ref_size = len(row)
                if len(row) != ref_size:
                    print("Error with file")
                    self.file = None
                    return None
                if any(not elem for elem in row):
                    print("Error with file")
                    self.file = None
                    return None
        except Exception:
            print("Error with file")
            return None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file and not self.file.closed:
            self.file.close()

    def getdata(self):
        datas_list = []
        with open(self.filename, 'r') as file:
            datas = csv.reader(file, delimiter=self.sep, skipinitialspace=True)
            for sub_list in datas:
                datas_list.append(sub_list)
            if self.header and len(datas_list) > 1:
                datas_list.pop(0)
            if self.skip_top != 0:
                if self.skip_top < len(datas_list):
                    datas_list = datas_list[self.skip_top:]
                else:
                    datas_list = []
            if self.skip_bottom != 0:
                if self.skip_bottom < len(datas_list):
                    datas_list = datas_list[:len(datas_list) - self.skip_bottom]
                else:
                    datas_list = []
        return datas_list

    def getheader(self):
        header = None
        if not self.header:
            return header
        with open(self.filename, 'r') as file:
            datas = csv.reader(file, delimiter=self.sep, skipinitialspace=True)
            header = next(datas)
        return header

