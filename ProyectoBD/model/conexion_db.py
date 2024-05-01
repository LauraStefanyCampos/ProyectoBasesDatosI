import mysql.connector

conexion = mysql.connector.connect(user='root', password='root', host='localhost', 
                                   database='proyectobd', port='3306')

print(conexion)