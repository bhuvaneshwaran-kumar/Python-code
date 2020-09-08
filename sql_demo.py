import sqlite3

# creates a connection between program and db
conn = sqlite3.connect('my_db.db')
# HELPS TO EXECUTES QUERY TO DATABASE
cursor = conn.cursor()

# creation of table
# cursor.execute( " create table students (id text primary key,name text,phone_number text) ")

id = '18BCS0060'
name = 'ragha'
no = '9846543210'

students = [
    ('18BCS0022','Vasanth','987654210'),
    ('18BCS0024','Kaviya','987654210'),
]

# for student in students:
#     cursor.execute(" insert into students values(:id ,:name ,:no)",
#                         {'id':student[0],'name':student[1],'no':student[2]})
#
# print("inserted row")

# retrive from DB
data = cursor.execute("select * from students")
print("Row Count: ",data.rowcount)

for row in data.fetchall():
    print(row)



# commits everything to tht DB
conn.commit()
conn.close() # close the connection
