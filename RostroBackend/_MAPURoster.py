import pandas
import datetime
import csv
from openpyxl import workbook, worksheet
from openpyxl.reader.excel import load_workbook

from RostroBackend.Roster import *

class MAPURoster(Roster):
    def __init__(self, rostername: str, username: str) -> None:
        super().__init__(rostername, username)
        self.df = self.load_roster_from_file()
        
        self.get_dates()
        self.get_indexes()
        self._find_shifts()

    def load_roster_from_file(self): # add return type
        df = pandas.read_excel(self.rostername)
        return df

    def print_roster(self) -> None:
        rows = self.df.iter_rows()
        for i in rows:
            for cell in i:
                print(cell.value)

    def get_indexes(self) -> None:
        '''finds every cell in a dataframe with the specified string in it and returns the cells as a list'''
        nameindexes = []
        res = self.df.isin([self.username])
        bool_series = res.any()
        col_names = list(bool_series[bool_series == True].index)
        for i, col in enumerate(col_names):
            rows = list(res[col][res[col] == True].index)
            for row in rows:
                nameindexes.append([i, row])
        self.nameindexes = nameindexes
        
        extract = []
        for i, position in enumerate(nameindexes):
            for rowindex, row in self.df.iterrows():
                if self.nameindexes[i][1] == rowindex:
                    extractrow = row
                    extract.append(extractrow)
        self.shiftrows = extract

    def get_dates(self) -> None:
        '''returns any datetime or pandas.Timestamp along with its index as a list of lists'''
        dates = []
        for rowindex, row in self.df.iterrows():
            for index, cell in enumerate(row):
                if type(cell) == pandas.Timestamp:
                    cell = cell.date()
                    dates.append([index,rowindex,cell])
        self.dates = dates

    def find_shifts(self):

        # for i, date in enumerate(self.dates):
        #     for ii, shift in enumerate(self.shiftrows):   
        #         for iii, cell in enumerate(shift):
        #             print(cell)

        date_indexes = [(date[0], date[2]) for date in self.dates]
        for shift in self.shiftrows:
            cols = [i for i, cell in enumerate(shift) if i in [d[1] for d in date_indexes]]
            cols = date_indexes[cols]
        print(cols)


    

    def _find_shifts(self):
        #code could be made more efficent by only scanning the pos row and below (until finding new relevant line)

        shifts = []

        for dateindex, date in enumerate(self.dates):
            for shiftrow in self.shiftrows:                
                for colindex, cell in enumerate(shiftrow):
                    if colindex == date[0]:
                        shiftdata = [colindex,date[2]]
                        shift_info_start = colindex
                        while dateindex+1 < len(self.dates) and colindex != self.dates[dateindex+1][0]:
                            shiftdata.append(shiftrow[colindex])
                            shift_info_length = colindex - shift_info_start
                            colindex = colindex + 1
                        if dateindex+1 == len(self.dates):
                            j = 0
                            while j <= shift_info_length:
                                shiftdata.append(shiftrow[colindex])
                                colindex = colindex + 1
                                j = j + 1
                        shifts.append(shiftdata)

        self.shifts = shifts
        print(self.shifts)

if __name__ == '__main__':

    mapu = MAPURoster('Roster.xls', 'James Lawson')
    print(mapu.shifts)
