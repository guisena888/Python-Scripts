'''
Script to run a massive process on your database
Read an excel file to get the data
'''

import os
from datetime import date
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlrd

df = pd.read_excel('excelFilename.xlsx', encoding='latin1')
print("Input the column name of the corresponding data ")
Name = input("Name: ")
Adress = input("Adress: ")
Age = input("Age: ")


total_rows = df.count
f = open("FinalScriptFile.sql", "w+")
for index, row in df.iterrows():
    f.write(
        "/*1*/INSERT INTO USERS VALUES('{Name}','{Adress}','{Age}'\n".format(
            Name=row[Name], Adress=row[Adress], Age=row[Age]))


f.close()




