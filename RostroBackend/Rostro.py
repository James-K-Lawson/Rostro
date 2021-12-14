import sys
import os
import csv
from openpyxl import workbook, worksheet
from openpyxl.reader.excel import load_workbook

from RostroBackend.Roster import *
# from Roster import *

# from RostroBackend.EDRoster import *
# from RostroBackend.MAPURoster import *

import argparse

class ArgumentParser(argparse.ArgumentParser):
    """ class for better argument parsing """
    def error(self, message):
        self.print_help(sys.stderr)
        self.exit(2, "%s: error: %s\n" % (self.prog, message))

def sort_roster(username: str, rosterpath: str):
    ros = Roster(username, rosterpath)
    return ros

if __name__ == "__main__":

    parser = ArgumentParser(description="args for Rostro")
    parser.add_argument("username", type=str, help="hint for username")
    parser.add_argument("rosterpath", type=str, help="hint for rostername")
    args = parser.parse_args()
    ed = sort_roster(args.username, args.rosterpath)
    ed.create_ical()