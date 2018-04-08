import sys
import os
from ING2YNAB.ING2YNAB import Ing2YNAB

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename_in = sys.argv[1]
        dir_out = sys.argv[2]
    elif len(sys.argv) == 1:
        filename_in = os.path.dirname(sys.argv[0]) + '\\transactions.csv'
        dir_out = os.path.dirname(sys.argv[0])

    converter = Ing2YNAB(filename_in, dir_out)
    converter.read()
    converter.write()
