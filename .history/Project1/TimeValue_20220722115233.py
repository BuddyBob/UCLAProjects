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
    #input validation loop
    while True:
            #If user entered special characters remove them except for decimal point
            x = float(re.sub('[^0-9.]+', '', input(f"{arg} ")))
            #Rate Validation - check if decimal point is first char (this means user entered percent in decimal form)
            #However, if decimal point is first but '%' is at end ignore if statement
            if ((arg == "Enter Rate (percent form %)" and str(x)[0] == '.') and (str(x)[-1] != '%')):
                print("Please enter your rate in percent form")
            else:
                break
        
    req_values.append(x)
    
        
    
        
        

#create object, pass in required values for chosen computation and call function
obj = TimeValue(*req_values)
getattr(obj, inv_comp)()
        
        
