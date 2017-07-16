import sys
import os
from ING2YNAB.ING2YNAB import Ing2YNAB

if __name__ == '__main__':
    if len(sys.argv) > 1:
        lv_filename_in = sys.argv[1]
        lv_dir_out = sys.argv[2]
    elif len(sys.argv) == 1:
        lv_filename_in = os.path.dirname(sys.argv[0]) + '\\transactions.csv'
        lv_dir_out = os.path.dirname(sys.argv[0]) 

    lr_converter = Ing2YNAB(lv_filename_in, lv_dir_out)
    lr_converter.read()
    lr_converter.write()
    
    
                