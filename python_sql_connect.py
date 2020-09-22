import pypyodbc as pyodbc
from datetime import datetime

db_host = r'srv-pine2016\fx2012'
db_name = 'standard9502'
db_user  = 'sa'
db_password  = 'Flexite123'

# connection_string = 'Driver={SQL Server Native Client 10.0};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
# db = pyodbc.connect(connection_string)
# db.close()

# cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};'
#                         'SERVER=' + db_host + ';'
#                         'DATABASE=' + db_name + ';'
#                         'UID=' + db_user + ';'
#                         'PWD=' + db_password + ';')
#
# сursor = cnxn.cursor()
#
# cnxn.close()


class Sql:
    def __init__(self, database, username, userpassword, server=db_host):
        self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 10.0};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "UID="+username+";"
                                   "PWD="+userpassword+';')
        self.query = "-- {}\n\n-- Made in Python".format(datetime.now()
                                                         .strftime("%d/%m/%Y"))
        print(self.query)


# try:
#     sql = Sql(db_name, db_user, db_password)
#     cursor = sql.cnxn.cursor()
#
#     mySQLQuery = ("""
#                      DELETE FROM ACT_HISTORY WHERE AH_ID in
#                      (SELECT  AH.AH_ID  FROM   REG_TD RT,  ACT_HISTORY AH  WHERE   RT.REGISTRATION_ID = 155   AND AH.AH_ID = RT.AH_ID    AND (RT.TD_TYPE IN (1, 2, 3)))
#                   """)
#     cursor.execute(mySQLQuery)
#     sql.cnxn.commit()
#     cursor.execute("select registration_id, name from REGISTRATION")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     sql.cnxn.close()
# except:
#     pass




