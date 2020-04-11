root_path = 'G:/Semester 8/FYP2'
dataset_path = root_path + '/dataset'
reports_path = root_path + '/Reports'
results_path = root_path + '/Results'

#for Debugging
#import  pdb; pdb.set_trace()

#for debugging 2, needs testing
#import code; code.interact(local=dict(globals(), **locals()))

# DataBase Columns VarChar Information
# Small Fields : 20
# general fields: 100
# long fields like title, description, requirements, major : 5000



# query to load data from external files quickly to mysql table
# load data infile 'apps.tsv' into table job_applications
# fields terminated by '\t'
# ;


