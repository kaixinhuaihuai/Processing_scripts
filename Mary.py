import pandas as pd
import glob
from openpyxl import load_workbook
import os
import csv
import xlrd

data = pd.DataFrame(columns = ["Participant_ID", "Type", "C1T1","C1T2","C1T3", "C2T1","C2T2","C2T3",\
"C3T1","C3T2","C3T3", "C4T1","C4T2","C4T3","C5T1","C5T2","C5T3","C6T1","C6T2","C6T3",\
"C7T1","C7T2","C7T3", "C8T1","C8T2","C8T3","C9T1","C9T2","C9T3"])
print (data)
index = 0
# get the csv files
path = "/home/phoenix*/Downloads"
files = glob.glob("%s/*.xlsx" %(path))


#csvs = glob.glob("%s/*.csv" %(path))
for file in files:                          # loop through them, for each file do:
    name = os.path.basename(file)                     # get the name of the file itself
    print(name)                                       # get subject ID from the file name
    ID = name[0:3]                                    # get the conditions and times respectively
    c1t1 = name[11:13] + "T1"
    c1t2 = name[11:13] + "T2"
    c1t3 = name[11:13] + "T3"
    c2t1 = name[13:15] + "T1"
    c2t2 = name[13:15] + "T2"
    c2t3 = name[13:15] + "T3"
    c3t1 = name[15:17] + "T1"
    c3t2 = name[15:17] + "T2"
    c3t3 = name[15:17] + "T3"
    print(c3t3)
    info = pd.DataFrame(pd.read_excel(name, header = None))
    print(info.loc[13,18])
    data.at[index,"Participant_ID"] = ID
    data.at[index, "Type"] = info.loc[13,9]
    data.at[index, c1t1] = info.loc[13,10]
    data.at[index, c1t2] = info.loc[13,11]
    data.at[index, c1t3] = info.loc[13,12]
    data.at[index, c2t1] = info.loc[13,13]
    data.at[index, c2t2] = info.loc[13,14]
    data.at[index, c2t3] = info.loc[13,15]
    data.at[index, c3t1] = info.loc[13,16]
    data.at[index, c3t2] = info.loc[13,17]
    data.at[index, c3t3] = info.loc[13,18]
    index = index + 1
    data.at[index,"Participant_ID"] = ID
    data.at[index, "Type"] = info.loc[44,9]
    data.at[index, c1t1] = info.loc[44,10]
    data.at[index, c1t2] = info.loc[44,11]
    data.at[index, c1t3] = info.loc[44,12]
    data.at[index, c2t1] = info.loc[44,13]
    data.at[index, c2t2] = info.loc[44,14]
    data.at[index, c2t3] = info.loc[44,15]
    data.at[index, c3t1] = info.loc[44,16]
    data.at[index, c3t2] = info.loc[44,17]
    data.at[index, c3t3] = info.loc[44,18]
    print(data)
    data.to_csv("master_file.csv")
# workbook.save("book1.xlsx")
