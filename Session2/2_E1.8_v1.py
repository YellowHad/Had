import sqlite3

if __name__ == '__main__':

    # Database file location
    url = 'C:\Users\Martin\Documents\WebDevelopment2\Lesson2'

    # Connect to Sqlite
    conn = sqlite3.connect(url+'\BanksAndTransactions.sqlite')

    # Cursor instance
    cursor = conn.cursor()


    #check whether tables have records
    cursor.execute('SELECT COUNT(*) AS NOBS FROM S_BANKS')
    row = cursor.fetchone()
    if row[0] == 0:
        cursor.execute('DROP TABLE S_BANKS')
    elif row is None:
        cursor.execute('DROP TABLE S_BANKS')

    # Create table S_BANKS
    sqlStmt = """CREATE TABLE S_BANKS 
                 (
                 PROCESSING_PERIOD      NUMERIC         NOT NULL
                ,TXT_BANK_SHORTNAME     VARCHAR(30)     NOT NULL
                ,TXT_BANK_LONGNAME      VARCHAR(250)    NOT NULL
                ,COD_BANK_CODE          VARCHAR(10)     NOT NULL
                ,COD_COUNTRY_DOMICIL    VARCHAR(2)      NOT NULL
                ,NAM_COUNTRY            VARCHAR(250)    NOT NULL
                ,COD_BANK_SYS_ID        VARCHAR(30)
                ,COD_BIC                VARCHAR(30)
                ,DAT_RECORD             DATETIME        DEFAULT CURRENT_TIMESTAMP
                ,UNIQUE (TXT_BANK_SHORTNAME, COD_BANK_CODE, COD_COUNTRY_DOMICIL)
                );"""

    cursor.execute(sqlStmt)

    cursor.execute("SELECT COUNT(*) AS NOBS FROM B_M_LOANS")
    row = cursor.fetchone()
    if row[0] == 0:
        cursor.execute('DROP TABLE B_M_LOANS')
    elif row is None:
        cursor.execute('DROP TABLE B_M_LOANS')

    # Create table B_M_LOANS
    sqlStmt = """
    CREATE TABLE B_M_LOANS
    (
        PROCESSING_PERIOD       NUMERIC     NOT NULL
       ,TXT_BANK_SHORTNAME      VARCHAR(30) NOT NULL
       ,AMT_AMOUNT              NUMERIC
       ,COD_CURRENCY            VARCHAR(3)
       ,RAT_INTEREST_RATE       FLOAT
       ,DAT_TRADE               DATETIME
       ,AMT_OPENED_TRADE_EXP    NUMERIC
       ,AMT_REPAID              NUMERIC
       ,AMT_INTEREST_REPAID     NUMERIC
       ,COD_LOAN_TYPE           VARCHAR(10)
       ,COD_DEPRECIATION        VARCHAR(1)
    )
    """

    cursor.execute(sqlStmt)
    conn.close()

