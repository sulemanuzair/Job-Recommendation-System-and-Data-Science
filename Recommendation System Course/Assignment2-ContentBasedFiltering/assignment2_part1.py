# Simple Content based filtering
import pandas as pd

import pymysql
domain = 'localhost'
username = 'root'
password = ''
db_name = 'jobs_system'
db = pymysql.connect(domain, username, password, db_name)

cursor = db.cursor()
total_job_applications_being_used = 10000

try:
    job_applications_sql         = 'select * from job_applications limit %d;' % total_job_applications_being_used
    cursor.execute(job_applications_sql)
    job_applications = cursor.fetchall()

    job_applications_columns_sql = 'select Column_name ' \
                                   'from Information_schema.columns ' \
                                   'where Table_name like "job_applications";'
    cursor.execute(job_applications_columns_sql)
    cols = cursor.fetchall()
    new_cols = []
    for each in cols:
        new_cols.append(each[0])
    job_applications_df = pd.DataFrame(job_applications, columns=new_cols)

    user_ids_sql = ', '.join(str(id) for id in job_applications_df.user_id)
    users_sql = 'select * from users where user_id in (%s)' % user_ids_sql
    cursor.execute(users_sql)
    users = cursor.fetchall()
    
    users_columns_sql = 'select Column_name ' \
                        'from Information_schema.columns ' \
                        'where Table_name like "users";'
    cursor.execute(users_columns_sql)
    cols = cursor.fetchall()
    new_cols = []
    for each in cols:
        new_cols.append(each[0])
    users_df = pd.DataFrame(users, columns=new_cols[0:-3]) # 3 extra column name also present in query output
    
    job_ids_sql = ', '.join(str(id) for id in job_applications_df.job_id)
    jobs_sql = 'select * from jobs where job_id in (%s)' % job_ids_sql
    cursor.execute(jobs_sql)
    jobs = cursor.fetchall()

    jobs_columns_sql = 'select Column_name ' \
                       'from Information_schema.columns ' \
                       'where Table_name like "jobs";'
    cursor.execute(jobs_columns_sql)
    cols = cursor.fetchall()
    new_cols = []
    for each in cols:
        new_cols.append(each[0])
    jobs_df = pd.DataFrame(jobs, columns=new_cols)
    
    print(users_df, jobs_df, job_applications_df)
except:
    print('Error: Exception catched manually.')
db.close()

