import re
from unittest.loader import VALID_MODULE_NAME

class TimeValue:
    def __init__(self, *args):
        self.args = args
        
    def PV(self):
        FV,r,n  = self.args
        return FV/(1+(r/100))**(n)
        
    def FV(self):
        PV,r,n  = self.args
        return PV*(1+(r/100))**(n)
    
    def Annuity(self):
        C,r,n  = self.args
        return C/(r/100) * ( 1- ( 1/ ( ( 1+ ( r/100 ) ) ** n) ) )
    
    def Perpetuity(self):
        C,r = self.args
        return C/r

#required values for each computation stored in dictionary
values_dict = {
    "PV":("Enter Future Value", "Enter Rate (percent form %)", "Enter number of months to hold deposit"),
    "FV":("Enter Present Value", "Enter Rate (percent form %)", "Enter number of months to hold deposit"),
    "Annuity":("Enter Cash Value", "Enter Rate (percent form %)", "Enter interest-compounding periods: "), 
    "Perpetuity":("Enter Cash Value", "Enter Rate (percent form %)")}
inv_comp = input("Enter a desired investment computation (PV, FV, Annuity, Perpetuity) ")

#iterate through required values for chosen computation and store input into req_values
req_values = []
for arg in values_dict[inv_comp]:
    inp = input(arg,' ')
    
            # x = float(re.sub('[^0-9.]+', '', x))
            
            

        
    req_values.append(x)
    
        
    
        
        

#create object, pass in required values for chosen computation and call function
obj = TimeValue(*req_values)
getattr(obj, inv_comp)()
        
        
