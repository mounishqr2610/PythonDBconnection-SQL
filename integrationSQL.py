import pyodbc  # this libraries used for DB connection
import pandas as pd  # this libraries is used to frame the data
conn = pyodbc.connect('Driver={SQL Server};'     # here giving all DB Details 
                      'Server=DESKTOP-J3J03MN;'
                      'Database=Pybot;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor() # fetch the data from the result set of the queries
conn.commit()  # to save the current transaction
cursor.execute('SELECT * FROM Pybot.dbo.rebot')   # execute the table
for row in cursor:
    print(row)
