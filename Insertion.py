def database_automation():

    import pyodbc

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-E0KD94T;'
                      'Database=RAZE;'
                      'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute('''
                INSERT INTO DEPARTMENT (DEPTCODE, DEPTNAME, LOCATION)
                VALUES
                (626,'FAN',120),
                (662266,'Tablet',300)
                ''')

    cursor = conn.cursor()
    #cursor.execute('SELECT * FROM DEPARTMENT')
    conn.commit()

