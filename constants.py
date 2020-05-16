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


# Create django auth users for dataset users
# Python shell command
# from django.contrib.auth.hashers import make_password
# Other Model needs to be included as well
pwd = make_password('password')
for user in User.objects.filter(auth_user_id = None):
	try:
		with transaction.atomic():
            user.auth_user = AuthUser.objects.create(
				username=str(user.id),
				email=str(user.id) + '@email.com',
				password=pwd,
				is_active=True
			)
			user.auth_user.save()
			user.save()
	except Exception as e:
		print('An error occured for user id '+ str(user.id) + ': ' + str(e))
