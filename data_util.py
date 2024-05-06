# This is a class about date format
from datetime import date
import os
import datetime

class data_solution:
    def __init__(self,datestr):
        self.datestr = datestr
    
    # get the current date
    def get_current_date(self):
        return date.today()
    
    # format the date
    def format_date(self):
        return self.datestr.strftime("%m/%d/%Y")

# today = date.today()
# date_util = data_solution(today)
# print(date_util.get_current_date())
# print(date_util.format_date())
dateinput = input("Which date do you input:? ")
date = datetime.strptime(dateinput, "%m/%d/%Y")
date_util = data_solution(date)
print(date_util.format_date())