
class RowReader(object):

    row = []

    def __init__(self, row):
        self.row = row
        
    def get_date(self):
        year = self.row[0][0:4]
        month = self.row[0][4:6]
        day = self.row[0][6:8]
        return day + '/' + month + '/' + year
    def get_payee(self):
        
        return self.row[1]

    def get_category(self): 
        return ''
    
    def get_memo(self):  

        return self.row[8]
       
    def get_outflow(self): 
        string = ''
        string = self.row[6]
        string = string.replace(',', '.')
         
        if self.row[5] == 'Af':
            return string
        else:
            return ''
                
    
    def get_inflow(self):
        string = ''
        string = self.row[6]
        string = string.replace(',', '.')
        
        if self.row[5] == 'Bij':
            return string
        else:
            return ''
