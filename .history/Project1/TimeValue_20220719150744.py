import re

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
        return C/(r/100) * 1-(1/(1+(r/100)) ** (n-1))
    
    def Perpetuity(self):
        C,r = self.args

#required values for each computation stored in dictionary
values_dict = {
    "PV":("Enter Future Value: ", "Enter Rate (%)", "Enter number of months to hold deposit: "),
    "FV":("Enter Present Value: ", "Enter Rate (%)", "Enter number of months to hold deposit: "),
    "Annuity":("Cash Value", "Rate (%)", "interest-compounding pesriods"), 
    "Perpetuity":("Cash Value", "Rate (%)")}
inv_comp = input("Enter a desired investment computation (PV, FV, Annuity, Perpetuity) ")

#iterate through required values for chosen computation and store input into req_values
req_values = []
for arg in values_dict[inv_comp]:
    #make sure user input is float or integer (eliminates the usage of '%' or letters in input)
    try:
        x = input(f"{arg}: ")
        req_values.append(float(x))
    except:
        req_values.append(float(re.sub('[^0-9.]+', '', x)))
        
        

#create object, pass in required values for chosen computation and call function
obj = TimeValue(*req_values)
getattr(obj, inv_comp)()
        
        
