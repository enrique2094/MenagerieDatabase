import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='Venezuela.2020')
cursor = conn.cursor()
cursor.close()
conn.close()
