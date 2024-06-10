import pyodbc

#conn = pyodbc.connect('DSN=your_dsn_name')

try:
    conn_str = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=45.249.111.177,12444;'
        'DATABASE=IMDB_DXP_JORDAN;'
        'UID=sa;'
        'PWD=CcwZMvGbAnxWg4c$;'
         'Encrypt=yes;'
        'TrustServerCertificate=yes;'
         
    )
    print(f"Connecting with connection string: {conn_str}")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT 1')
    print(cursor.fetchone())
except pyodbc.Error as e:
    print("Error in connection:", e)

