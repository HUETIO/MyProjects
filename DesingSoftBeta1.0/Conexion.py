from fileinput import close
import mysql.connector
class conexion:
 def __init__(self):
     self.connection=mysql.connector.connect(user="root",password="",
                                    host="localhost",
                                    database="desingsoftdata",
                                    port="3306")
     self.cursor=self.connection.cursor()
