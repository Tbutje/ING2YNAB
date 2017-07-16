
class RowReader(object):

    ms_row = []
    coDiverseBoekingen      = 'DV'
    
#   not checked yet    
    coCrediteurenBetaling   = 'cb'
    coGeldAutomaat          = 'ga'
    coBetaalAutomaat        = 'ba'
    coBetaalContactLoos     = 'bc'
    coBankGiro              = 'bg'
    coEuroIncasso           = 'ei'
    coIdeal                 = 'id'
    coEigenRek              = 'tb'

    def __init__(self, row):
        self.ms_row = row
        
    def get_date(self):
        lv_year = self.ms_row[0][0:4]
        lv_month = self.ms_row[0][4:6]
        lv_day = self.ms_row[0][6:8]
        return lv_day + '/' + lv_month + '/' + lv_year
    def get_payee(self):
        lv_pay_type = self.ms_row[4]
        
        if ( lv_pay_type == self.coGeldAutomaat
        or   lv_pay_type == self.coBetaalAutomaat
        or   lv_pay_type == self.coBetaalContactLoos):
            return self.ms_row[10]  
        
        elif (  lv_pay_type == self.coBankGiro
             or lv_pay_type == self.coCrediteurenBetaling
             or lv_pay_type == self.coEuroIncasso
             or lv_pay_type == self.coIdeal
             or lv_pay_type == self.coEigenRek):
            return self.ms_row[5] + " - " + self.ms_row[6]
        
        elif lv_pay_type == self.coDiverseBoekingen:
            return self.ms_row[1]

        else:
            return self.ms_row[5]
          
   
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
