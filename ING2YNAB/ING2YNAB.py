import csv, sys
from ING2YNAB.RowReader import RowReader

class Ing2YNAB(object):
    
    mt_data = []   

    def __init__(self, file_in, dir_out):
        self.mv_file_in = file_in
        self.mv_dir_out = dir_out
        
        
        
        
    def read(self):
        try:
            with open(self.mv_file_in) as File:
#               just to skip first line  
                lv_first_line = File.readline()
                lr_reader = csv.reader(File)
                for ls_row in lr_reader:
                    lr_rowReader = RowReader(ls_row) 
   
                    ls_data = { 'date':     lr_rowReader.get_date(),
                               'payee':     lr_rowReader.get_payee(),
                               'category':  lr_rowReader.get_category(),
                                'memo':     lr_rowReader.get_memo(),
                                'out':      lr_rowReader.get_outflow(),
                                'in':       lr_rowReader.get_inflow() }
                    self.mt_data.append(ls_data)
                        
        except IOError:
            sys.exit( "input file error",
                      "input file not found\nplease check the input file name")
                
    
    def write(self):
        ls_data = {}
        if self.mv_dir_out.find('\\') > 0:
            lv_filename = self.mv_dir_out + '\\' + 'ING' + '.csv'
        else:
            lv_filename = self.mv_dir_out + 'ING' + '.csv'
        
        try:
            with open(lv_filename, 'w+', newline='') as lr_file:
                lr_writer = csv.writer(lr_file, quoting=csv.QUOTE_NONNUMERIC)
                
#                   write header row
                lr_writer.writerow([ 'Date' , 'Payee' , 'Category' , \
                                  'Memo' , 'Outflow' , 'Inflow' ])
            
#                   write the rest
                for jdx, ls_data in enumerate(self.mt_data):
                    lr_writer.writerow([ls_data.get('date'), \
                                        ls_data.get('payee'), \
                                        ls_data.get('category'), \
                                        ls_data.get('memo'), \
                                        ls_data.get('out'), \
                                        ls_data.get('in')])
        except IOError:
            sys.exit( "Output file error" )
    
      
        