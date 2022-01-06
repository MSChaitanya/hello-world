import pandas as pd
import pyodbc 

server = 'DESKTOP-6VIF0AE' 
database = 'AdventureWorks2019' 
username = 'sa' 
password = 'sa@123' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# cursor = cnxn.cursor()
# cursor.execute('Select * from Sales.Customer')

df = pd.read_sql_query('Select * from Sales.Customer', cnxn)

print(df)
print(type(df))
