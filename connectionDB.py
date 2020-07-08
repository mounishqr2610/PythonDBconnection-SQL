import pyodbc  # this libraries used for DB connection
import pandas as pd  # this libraries is used to frame the data
conn = pyodbc.connect('Driver={SQL Server};'     # here giving all DB Details 
                      'Server=DESKTOP-J3J03MN;'
                      'Database=Pybot;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
#cursor.execute("""INSERT INTO rebot values (4,'RamC#','Dynamics , C#,Python,SQL,JS','B.Tech','Senior Software','3 year')""")
conn.commit()
#cursor.execute('SELECT * FROM Pybot.dbo.rebot')
SQl_query = pd.read_sql_query('SELECT * FROM Pybot.dbo.rebot',conn) #Data frame using Pandas
print(SQl_query)
#for row in cursor:
 #   print(row)
#sql_query = pd.read_sql_query('SELECT * FROM Pybot.dbo.rebot',conn)
#print(sql_query)
#print(type(sql_query))