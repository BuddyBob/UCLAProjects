{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'TimeValue' object has no attribute 'locals'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m/Users/thavas/Documents/UCLA/Project1/TimeValue.ipynb Cell 2'\u001b[0m in \u001b[0;36m<cell line: 40>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     <a href='vscode-notebook-cell:/Users/thavas/Documents/UCLA/Project1/TimeValue.ipynb#ch0000000?line=36'>37</a>\u001b[0m \u001b[39m#create object, pass in required values for chosen computation and call function\u001b[39;00m\n\u001b[1;32m     <a href='vscode-notebook-cell:/Users/thavas/Documents/UCLA/Project1/TimeValue.ipynb#ch0000000?line=37'>38</a>\u001b[0m obj \u001b[39m=\u001b[39m TimeValue(\u001b[39m*\u001b[39mreq_values)\n\u001b[0;32m---> <a href='vscode-notebook-cell:/Users/thavas/Documents/UCLA/Project1/TimeValue.ipynb#ch0000000?line=39'>40</a>\u001b[0m \u001b[39mprint\u001b[39m(obj\u001b[39m.\u001b[39;49mlocals()[\u001b[39m\"\u001b[39m\u001b[39minv_comp\u001b[39m\u001b[39m\"\u001b[39m]())\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'TimeValue' object has no attribute 'locals'"
     ]
    }
   ],
   "source": [
    "\n",
    "class TimeValue:\n",
    "    def __init__(self, *args):\n",
    "        self.args = args\n",
    "    def PV(self):\n",
    "        FV,r,n  = self.args\n",
    "        return f\"$ {FV/(1+(r/100))**(n):.3f}\"\n",
    "        \n",
    "    def FV(self):\n",
    "        PV,r,n  = self.args\n",
    "        return f\"$ {PV*(1+(r/100))**(n):.3f}\"\n",
    "    def Annuity(self):\n",
    "        C,r,n  = self.args\n",
    "        return f\"$ {(C/(r/100)) * (1-(1/(1+(r/100)) ** (n-1))):.3f}\"\n",
    "    def Perpetuity(self):\n",
    "        C,r = self.args\n",
    "\n",
    "#required values for each computation stored in dictionary\n",
    "values_dict = {\n",
    "    \"PV\":(\"Future Value\", \"Rate (%)\", \"interest-compounding periods\"),\n",
    "    \"FV\":(\"Present Value\", \"Rate (%)\", \"interest-compounding periods\"),\n",
    "    \"Annuity\":(\"Cash Value\", \"Rate (%)\", \"interest-compounding pesriods\"), \n",
    "    \"Perpetuity\":(\"Cash Value\", \"Rate (%)\")}\n",
    "inv_comp = input(\"Enter a desired investment computation (PV, FV, Annuity, Perpetuity) \")\n",
    "\n",
    "#iterate through required values for chosen computation and store input into req_values\n",
    "req_values = []\n",
    "for arg in values_dict[inv_comp]:\n",
    "    #make sure user input is float or integer (eliminates the usage of '%' or letters)\n",
    "    try:\n",
    "        x = input(f\"{arg}: \")\n",
    "        req_values.append(float(x))\n",
    "    except:\n",
    "        req_values.append(float(re.sub('[^0-9.]+', '', x)))\n",
    "        \n",
    "        \n",
    "\n",
    "#create object, pass in required values for chosen computation and call function\n",
    "obj = TimeValue(*req_values)\n",
    "print(obj.locals()[\"inv_comp\"]())\n",
    "        \n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.0 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "7e1998ff7f8aa20ada591c520b972326324e5ea05489af9e422744c7c09f6dad"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
