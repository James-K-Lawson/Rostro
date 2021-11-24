from pandas import to_datetime
import csv
from openpyxl import workbook, worksheet
from openpyxl.reader.excel import load_workbook
import os

# RosterType
#     -> EDRoster
#     -> MAPURosteMAPURoster
# Interface


class Roster():
    def __init__(self, username: str, rosterpath: str) -> None:
        self.rosterpath = rosterpath
        self.rostername = os.path.basename(rosterpath)
        self.username = username
        self.nameindexes = None
        self.df = None
        self.dates = None
        self.shiftrows = None
        self.shifts = None
        self.roster_type = None

    def format_dates(self):
        for shift in self.shifts:
         for i in range(2,4):
            if type(shift[i]) == str:
                try:
                    shift[i] = int(shift[i])
                except:
                    print('cannot convert cell to int')
                    pass
            if type(shift[i]) == float or int:
                try:
                    shift[i] = to_datetime(shift[i], format ='%H%M').time()
                except:
                    print('non convertible float or int')
                    pass
        print(self.shifts)
    
    def create_csv(self):

        cols = ['Subject', 'Start Date', 'Start Time', 'End Time', 'Description']

        with open('RosterRead.csv', 'w') as f:
            write = csv.writer(f)

            write.writerow(cols)
            write.writerows(self.shifttable)
        

