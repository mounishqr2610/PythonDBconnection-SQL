import pyodbc  # this libraries used for DB connection
import pandas as pd  # this libraries is used to frame the data
conn = pyodbc.connect('Driver={SQL Server};'     # here giving all DB Details 
                      'Server=DESKTOP-J3J03MN;'
                      'Database=Pybot;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
s = "create table bot(id int primary key , Resumename varchar(200) , Skills varchar(50),Qualification varchar(50),Role varchar(50),Experience varchar(50))"
#cursor.execute(s)

#cursor.execute("""INSERT INTO bot values (4,'RamC#','Dynamics , C#,Python,SQL,JS','B.Tech','Senior Software','3 year')""")

conn.commit()
#cursor.execute('SELECT * FROM Pybot.dbo.bot')
SQl_query = pd.read_sql_query('SELECT * FROM Pybot.dbo.bot',conn)
print(SQl_query)
