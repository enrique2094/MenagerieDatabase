import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='Venezuela.2020', database='menagerie')
cursor = conn.cursor()
select_query = "SELECT * FROM pet WHERE species ='dog' AND sec='f'"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()
