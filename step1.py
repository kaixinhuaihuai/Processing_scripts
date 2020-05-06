import pandas as pd
import glob
from openpyxl import load_workbook
import os
import csv
import xlrd

path = "/home/phoenix*/Downloads"
files = glob.glob("%s/*.xlsx" %(path))


for file in files:
    workbook = load_workbook(filename = file)           # load the file as excel object
    info = workbook.active
    info.move_range("J37:S37", rows = 12, cols = 0)       # move the columns you don't need anymore
    info.move_range("J38:S38", rows = 12, cols = 0)
    info.move_range("J39:S39", rows = 12, cols = 0)
    workbook.save(filename = file)

for file in files:
    name = os.path.basename(file)
    book = xlrd.open_workbook(file)
    sh = book.sheet_by_index(0)
    with open(name + ".csv", "wb") as f:
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))
