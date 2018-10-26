import sqlite3


# Homework
def list_data_from_artist(c):
    SqlQuery = "SELECT name FROM artist"
    return c.execute(SqlQuery)


def list_data_from_invoice(c):
    SqlQuery = "SELECT * FROM invoice WHERE UPPER(billingCountry) = 'GERMANY'"
    return c.execute(SqlQuery)


def list_data_from_albums(c):
    SqlQuery = "SELECT COUNT(*) AS nobs FROM album"
    return c.execute(SqlQuery)


def list_data_from_customers(c):
    SqlQuery = "SELECT COUNT(*) AS nobs FROM customer WHERE UPPER(country) = 'FRANCE'"
    return c.execute(SqlQuery)


if __name__ == "__main__":
    directory = "C:\Users\Martin\Documents\WD2\Lesson1"
    conn = sqlite3.connect(directory+"\Chinook_Sqlite.sqlite")

    for x in list_data_from_artist(conn.cursor()):
        print(x)

    for x in list_data_from_invoice(conn.cursor()):
        print(x)

    for x in list_data_from_albums(conn.cursor()):
        print(x)

    for x in list_data_from_customers(conn.cursor()):
        print(x)

    conn.close()
