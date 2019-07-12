import cx_Oracle as cx
import pandas as pd
import time
from pyexcelerate import Workbook
import os

start = time.time()

print("Conecting to the database")
dsnStr = cx.makedsn(hostname, port, SID)
con = cx.connect(user="", password="", dsn=dsnStr, encoding='utf-8')

print("Connection estabilished")


date = time.strftime('%Y.%m.%d', time.localtime(time.time()))
file = "DirName "+ date
os.mkdir(file)


script = open('query.sql')
sql = script.read()
script.close()

#Query should look like this: SELECT * FROM TABLE WHERE ID = ?

parameter = ""
query = sql.replace('?', parameter)

print('Executing query')
df = pd.read_sql(query, con)
print("Exporting to excel file")
values = [df.columns] + list(df.values)
wb = Workbook()
wb.new_sheet('report', data=values)
wb.save(file+"/fileName")


con.close()
