import csv
import sys

from ING2YNAB.RowReader import RowReader


class Ing2YNAB(object):
    data_in = []

    def __init__(self, file_in, dir_out):
        self.file_in = file_in
        self.dir_out = dir_out

    def read(self):
        try:
            with open(self.file_in) as File:
                #               just to skip first line
                lv_first_line = File.readline()
                csvReader = csv.reader(File)
                for row in csvReader:
                    rowReader = RowReader(row)

                    data_row = {'date': rowReader.get_date(),
                                'payee': rowReader.get_payee(),
                                'category': rowReader.get_category(),
                                'memo': rowReader.get_memo(),
                                'out': rowReader.get_outflow(),
                                'in': rowReader.get_inflow()}
                    self.data_in.append(data_row)

        except IOError:
            sys.exit("input file error",
                     "input file not found\nplease check the input file name")

    def write(self):

        filename = self.dir_out

        try:
            data_row = {}
            with open(filename, 'w+', newline='') as file:
                lr_writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)

                #                   write header row
                lr_writer.writerow(['Date', 'Payee', 'Category',
                                    'Memo', 'Outflow', 'Inflow'])

                #                   write the rest
                for jdx, data_row in enumerate(self.data_in):
                    lr_writer.writerow([data_row.get('date'),
                                        data_row.get('payee'),
                                        data_row.get('category'),
                                        data_row.get('memo'),
                                        data_row.get('out'),
                                        data_row.get('in')])
        except IOError:
            sys.exit("Output file error")
