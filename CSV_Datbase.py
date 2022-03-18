def csv_insertion():
        import pyodbc
        import pandas as pd
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-E0KD94T;'
                      'Database=RAZE;'
                      'Trusted_Connection=yes;')


        cursor = conn.cursor()
        csv_file_nm='C:\\Users\\DELL\\OneDrive\\Documents\\CityTemperature_www.csv'
        db_table_nm='DEPARTMENT'
        data = pd.read_csv (r'C:\\Users\\DELL\\OneDrive\\Documents\\CityTemperature_www.csv')
        df = pd.DataFrame(data)
        for row in df.itertuples():
         cursor.execute('''
                    INSERT INTO DEPARTMENT (DEPTCODE, DeptName, LOCATION)
                    VALUES (?,?,?)
                    ''',
                    row.DEPTCODE,
                    row.DeptName,
                    row.LOCATION
                    )

         conn.commit()