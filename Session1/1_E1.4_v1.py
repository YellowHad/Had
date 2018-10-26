import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="MySql01",
  database="wob02"
)

cursor = mydb.cursor()
stmt = "SHOW DATABASES"
cursor.execute(stmt)

if __name__ == "__main__":
  for x in cursor:
    print(x)
