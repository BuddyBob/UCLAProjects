import re

class TimeValue:
    def __init__(self, *args):
        self.args = args
        # args list of (Future Value, Present Value, rate, n = time)
    def PV(self):
        FV,r,n  = self.args
        return round(FV/(1+(r/100))**(n),2)
        
    def FV(self):
        PV,r,n  = self.args
        return round(PV*((1+(r/100))**(n)),2)
    
    def Annuity(self):
        C,r,n  = self.args
        return round(C/(r/100) * ( 1- ( 1/ ( ( 1+ ( r/100 ) ) ** n) ) ),2)
    
    def Perpetuity(self):
        C,r = self.args
        return round(C/r,2)

inv_comp = input("Enter a desired investment computation (PV, FV, Annuity, Perpetuity) ")

#clarify with user what units to use for calculation (months, years)
unit = input("What units do you want to use for calculation (months, years)? ")

#required values for each computation stored in dictionary
values_dict = {
    "PV":("Enter Future Value", "Enter Rate (percent form %)", f"Enter number of {unit} to hold deposit"),
    "FV":("Enter Present Value", "Enter Rate (percent form %)", f"Enter number of {unit} to hold deposit"),
    "Annuity":("Enter Cash Value", "Enter Rate (percent form %)", f"Enter interest-compounding periods ({unit}): "), 
    "Perpetuity":("Enter Cash Value", "Enter Rate (percent form %)")}

#iterate through required values for chosen computation and store input into req_values
req_values = []
i = 0
while i < len(values_dict[inv_comp]):
    arg = values_dict[inv_comp][i]
    inp = input(str(arg)+' ')
    #Rate validation
    
    #if starts with decimal point ask user to input percent form
    #However allow 0.20 (0 before decimal) > .0020
    if inp.startswith(".") and arg == "Enter Rate (percent form %)":
        print("Please input your rate in percent form")
        continue
    
    #remove special characters such as % from Rate or commas from Cash Value
    n_inp = float(re.sub('[^0-9.]+', '', inp))
    #check if there was a change to inp > inform the user about this change
    if n_inp != inp:
        print('Your input has been changed from',inp,'to',n_inp)
    i += 1
                    
    req_values.append(n_inp)
    

#create object, pass in required values for chosen computation and call function
obj = TimeValue(*req_values)
print(inv_comp,getattr(obj, inv_comp)())
        
        
