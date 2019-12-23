import pymysql

domain = 'localhost'
username = 'root'
password = ''
db_name = 'web_project_db'
table_name = 'posts_job'
db = pymysql.connect(domain, username, password, db_name)

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print('Database version : %s ' % data)

sql_fetch_jobs = "SELECT * " \
      "FROM %s " \
      "WHERE id > '%d';" % (table_name, 1)
print(sql_fetch_jobs)
sql_table_structure = "describe %s;" % table_name
try:
    cursor.execute(sql_table_structure)
    structure = cursor.fetchall()
    print(structure)

    column_to_show = structure[1][0] # Job Title in this case
    cursor.execute(sql_fetch_jobs)
    jobs = cursor.fetchall()
    for row in jobs:
        title = row
        print(title[1])
except:
    print('Error: unable to fetch data')
db.close()
