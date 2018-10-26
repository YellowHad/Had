# List table field names
import sqlite3

if __name__ == "__main__":

    directory = "C:\Users\Martin\Documents\WD2\Lesson1"

    conn = sqlite3.connect(directory + "\Chinook_Sqlite.sqlite")

    SqlCommand = "SELECT * FROM INVOICE"

    c = conn.cursor().execute(SqlCommand)

    listOfFields = [description[0] for description in c.description]

    for y in listOfFields:
        print(y)

    conn.close()