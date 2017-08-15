
class RowReader(object):

    ms_row = []

    def __init__(self, row):
        self.ms_row = row
        
    def get_date(self):
        lv_year = self.ms_row[0][0:4]
        lv_month = self.ms_row[0][4:6]
        lv_day = self.ms_row[0][6:8]
        return lv_day + '/' + lv_month + '/' + lv_year
    def get_payee(self):
        
        return self.ms_row[1]

    def get_category(self): 
        return ''
    
    def get_memo(self):  

        return self.ms_row[8]
       
    def get_outflow(self): 
        lv_string = ''
        lv_string = self.ms_row[6]
        lv_string = lv_string.replace(',', '.') 
         
        if self.ms_row[5] == 'Af':
            return lv_string
        else:
            return ''
                
    
    def get_inflow(self):
        lv_string = ''
        lv_string = self.ms_row[6]
        lv_string = lv_string.replace(',', '.')  
        
        if self.ms_row[5] == 'Bij':
            return lv_string
        else:
            return ''
