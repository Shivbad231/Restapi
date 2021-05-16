import sqlite3

from sqlite3 import Error

def sql_connection():
   try:
     conn = sqlite3.connect('mydatabase.db')
     return conn
   except Error:
     print(Error)

def sql_table(conn):
   cursorObj = conn.cursor()
# Create the table
   cursorObj.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
# Insert the records
   cursorObj.executescript("""
   INSERT INTO salesman VALUES(5001,'Aniket','Pune', 0.55);
   INSERT INTO salesman VALUES(5002,'Shivam','Surat', 0.45);
   INSERT INTO salesman VALUES(5003,'Vishal','Chennai', 0.60);
   INSERT INTO salesman VALUES(5004,'Vijay','Hyderabad', 0.50);
   INSERT INTO salesman VALUES(5005,'Abhinav','Bangalore', 0.45);
   """)
   conn.commit()

   cursorObj.execute("UPDATE salesman SET name='Anand' WHERE city='Bangalore'")
   cursorObj.execute("SELECT * FROM salesman")
   rows = cursorObj.fetchall()
   print("Agent details:")
   for row in rows:
       print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")
