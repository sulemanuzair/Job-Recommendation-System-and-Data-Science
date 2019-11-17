#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","web_project_db" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#print ("Database version : %s " % data)


####

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM posts_job # \
      #WHERE id > '%d'" % (1)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   #print (results)
   for row in results:
      print(row)
      fname = row[0]
      #lname = row[1]
      #age = row[2]
      #sex = row[3]
      #income = row[4]
      # Now print fetched result
      print (fname)#("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
      #   (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")




####




# disconnect from server
db.close()