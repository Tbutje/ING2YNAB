import csv
import sys

from ing2ynab.RowReader import RowReader


class Ing2ynab(object):
    data_out = []
    data_in = []

    def __init__(self, data):
        self.data_in = data

    @classmethod
    def fromfilename(cls, file_in):
        data = []
        try:
            with open(file_in) as File:
                #               just to skip first line
                lv_first_line = File.readline()
                csvReader = csv.reader(File)
                for row in csvReader:
                    data.append(row)
        except IOError:
            sys.exit("input file error",
                     "input file not found\nplease check the input file name")
        return cls(data=data)

    @classmethod
    def fromlist(cls, data):
        return cls(data=data)

    def convert(self):
        for row in self.data_in:
            rowReader = RowReader(row)
            data_row = {'Date': rowReader.get_date(),
                        'Payee': rowReader.get_payee(),
                        'Category': rowReader.get_category(),
                        'Memo': rowReader.get_memo(),
                        'Outflow': rowReader.get_outflow(),
                        'Inflow': rowReader.get_inflow()}
            self.data_out.append(data_row)

    def to_csv(self, outputfile):

        try:
            data_row = {}
            with open(outputfile, 'w+', newline='') as file:
                lr_writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)

                #                   write header row
                lr_writer.writerow(['Date', 'Payee', 'Category',
                                    'Memo', 'Outflow', 'Inflow'])

                #                   write the rest
                for jdx, data_row in enumerate(self.data_out):
                    lr_writer.writerow([data_row.get('Date'),
                                        data_row.get('payee'),
                                        data_row.get('Category'),
                                        data_row.get('Memo'),
                                        data_row.get('Outflow'),
                                        data_row.get('Inflow')])
            print("Wrote output to: " + outputfile)
        except IOError:
            sys.exit("Output file error")
