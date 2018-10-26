import sqlite3

if __name__ == '__main__':

    # define directory where SQLITE files are stored
    directory = "C:\Users\Martin\Documents\WD2\Lesson1"

    # connect to SQLITE
    conn = sqlite3.connect(directory + "\Chinook_Sqlite.sqlite")

    # create cursor object
    cursor = conn.cursor()

    # Define SQL command
    SqlCommand = "SELECT name FROM artist"

    # Execute SQL command
    cursor.execute(SqlCommand)

    # Fetch all data
    # print(cursor.fetchall())

    #Loop through the cursor results
    for x in cursor.execute(SqlCommand):
        print(x)