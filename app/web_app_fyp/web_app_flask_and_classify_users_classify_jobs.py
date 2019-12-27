from constants import *
from sklearn import tree
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier

data =pd.read_csv("JobsClusters.tsv", sep='\t')
data = data[0:int(len(data)*0.05)]

scaler=preprocessing.MinMaxScaler()

data['Title']=data['Title'].fillna(value="None")
data['Description']=data['Description'].fillna(value="None")
data['Requirements']=data['Requirements'].fillna(value="None")

tr = data[['Title','Description','Requirements']]

data_job = data
aew = tr.Title+' '+tr.Description+' '+tr.Requirements

dataset_job = pd.DataFrame({'Combine':aew[:]})

v_job = TfidfVectorizer()
x_job = v_job.fit_transform(dataset_job['Combine'])

Hclustering = KMeans(n_clusters=4)
            
output = Hclustering.fit_predict(x_job)
dat = pd.DataFrame({'ClusterJob':output[:]})

y_job = tr.join(dat)

ann_job = MLPClassifier()#hidden_layer_sizes=100, alpha=0.005, activation='logistic' )
ann_job=ann_job.fit(x_job,y_job['ClusterJob'])
data1 =pd.read_csv(dataset_path + '/users/users_part.tsv', sep='\t')


scaler=preprocessing.MinMaxScaler()

data1['Major']=data1['Major'].fillna(value="None")
tr=data1['Major']
v = TfidfVectorizer()
x = v.fit_transform(tr)

y = v.transform(tr)
 
print ('y', y) 
print ('tr', tr) 
print ('x', x)        
            
Hclustering = KMeans(n_clusters=30)
output = Hclustering.fit_predict(x)

dataset = pd.DataFrame({'ClusterJob':output[:]})
st = pd.DataFrame(tr)
y = st.join(dataset)

print(y.info())

ann = MLPClassifier()#hidden_layer_sizes=100, alpha=0.005, activation='logistic' )
ann=ann.fit(x,y['ClusterJob'])

testKr = pd.DataFrame(['Computer Science',
                       'Electrical Engineer',
                       'Cables of the city'
                       ])
testKr.columns = [''] * len(testKr.columns)
testKr1 = v.transform(['Cable of the city'])
print ('transformed object', testKr1 , 'object ended')

predictValues= ann.predict(testKr1)

print(predictValues)        
print (y['ClusterJob'])

data = pd.read_csv("UserClusters.tsv", sep='\t')

data.drop(['Unnamed: 0'], axis = 1, inplace = True)
data.drop(['UserID'], axis = 1, inplace = True)
data.drop(['WindowID'], axis = 1, inplace = True)
data.drop(['Split'], axis = 1, inplace = True)
data.drop(['State'], axis = 1, inplace = True)
data.drop(['Country'], axis = 1, inplace = True)
data.drop(['ZipCode'], axis = 1, inplace = True)
data.drop(['User_Major_Cluster'], axis = 1, inplace = True)
data.drop(['ClusterUser'], axis = 1, inplace = True)
data.drop(['City'], axis = 1, inplace = True)

label=data['User_Education_Work_Cluster']
data.drop(['User_Education_Work_Cluster'], axis = 1, inplace = True)

dct = tree.DecisionTreeClassifier()
dct=dct.fit(data, label)



# update
testKr = pd.DataFrame([[	92262,	1,	5,	5.0,	0,	0]])
predictValues=dct.predict(testKr)


print(predictValues)        
data =pd.read_csv("UserClusters.tsv", sep='\t')
print (len(data))
data.loc[len(data)] = [len(data),	352740,	6,	0, 'Columbus','IN',	'US',		92262,	1,	5,	5.0,	0,	0,	0,	0,	predictValues[0],	predictValues[0]]
print (len(data))
data.to_csv("UserClustersAdded.tsv", sep ='\t', index = False)





from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd


users = pd.read_csv('UserClusters.tsv', sep='\t')

apps = pd.read_csv('ClusterWiseJobs.tsv', sep='\t')

jobs = pd.read_csv('JobsClusters.tsv', sep='\t')

def find_user_cluster(user_id):
    global users
    
    selected_row =  (users.loc[users['UserID'] == user_id])    
    user_cluster = selected_row['ClusterUser']
    user_cluster = user_cluster.reset_index(drop=True)
    return user_cluster[0]


def find_jobs(user_cluster):
    global apps
    selected_rows =  (apps.loc[apps['ClusterUser'] == user_cluster])
    jobs = selected_rows['JobID']
    jobs = jobs.reset_index(drop=True)
    
    return jobs

def find_jobs_details(job_ids):
    global jobs
    
    jobs_return = jobs.loc[jobs['JobID'].isin(job_ids)]
    return jobs_return
    

def get_recommended_jobs(user_id):
    
    print ('User ID : ', user_id)
    
    user_cluster_id = find_user_cluster(user_id)
    print ('User Cluster : ', user_cluster_id)
    
    job_ids = find_jobs(user_cluster_id)
    print ('Job Ids : ', job_ids)
    
    
    jobs_details = find_jobs_details(job_ids)
    print ('Recommended Jobs : ', jobs_details)
    
    jobs_details.to_csv("checking.csv")
        
    
    
    return jobs_details


user_id = 7928
jobs1 = get_recommended_jobs(user_id)

# =============================================================================
# @app.route("/")
# def index():
#     user_id = 7928
#     jobs1 = get_recommended_jobs(user_id)
# 
#     data = jobs1.values.tolist()
#     return render_template('index.html',  data=data)
#  
#     
# @app.route("/about")
# def about():
# 	return render_template('about.html')
# 
# 
# @app.route("/contact")
# def contact():
# 	return render_template('contact.html')
# 
# 
# 
# #@app.route("/jobDetails")
# #def jobDetails():
#  #   jobID = request.args.get('id')
#   # 
#    # return render_template('jobDetails.html',jobID=jobID)
# 
# 
# @app.route("/jobDetails")
# def jobDetails():
#     jobID = int(request.args.get('id'))
#     jobID_pass = [jobID]
#     job_details = find_jobs_details(jobID_pass)
#     job_details = job_details.reset_index(drop=True)
#     #print(job_details)
#     required_job = job_details.iloc[0]
#     
#     #print(required_job)
#     required_job = required_job.values.tolist()
#     #print(required_job)
#     
#     return render_template('jobDetails.html',jobID=required_job)
# 
# 
# 
# @app.route("/login")
# def login():
# 	return render_template('login.html')
# 
# 
# @app.route("/signUp")
# def signUp():
# 	return render_template('signup.html')
# 
# @app.route("/register", methods=['POST','GET'])
# def register():
# 	if request.method=='POST':
# 		name=request.form['name']
# 		email=request.form['email']
# 		password=request.form['password']
# 		#repeatPassword=request.form['repeatPassword']
# 		
# 		city = request.form['city']
# 		state = request.form['state']		
# 		country = request.form['country']
# 
# 		degreeType=request.form['degreeType']
# 		major=request.form['major']
# 		
# 		completionDate=request.form['completionDate']
# 		jobTitle = request.form['jobTitle']
# 		experience = request.form['experience']
# 		
# 		currentlyEmployee=request.form['currentlyEmployee']
# 		managedOthers=request.form['managedOthers']
# 		managedHowMany=request.form['managedHowMany']
# 
# 
# 		if (degreeType == 'None'):
# 		    degreeType = 0
# 		elif (degreeType == "Bachelor's"):
# 		    degreeType = 4 
# 		elif (degreeType == "Associate's"):
# 		    degreeType = 3 
# 		elif (degreeType == "Masters's"):
# 		    degreeType = 5 
# 		elif (degreeType == 'High School'):
# 		    degreeType = 1 
# 		elif (degreeType == 'Vocational'):
# 		    degreeType = 2 
# 		elif (degreeType == 'PhD'):
# 		    degreeType = 6 
# 		else:
# 		    degreeType = 1
# 		
#         #degreeType = map({'None': 0, "Bachelor's": 4, "Associate's": 3, "Master's": 5, "High School": 1, "PhD": 6, "Vocational": 2})
# 		print(degreeType)
# 		#print (managedHowMany)
# 		#print (managedOthers)
#         
# 
# 		testKr = pd.DataFrame([[ degreeType,	1,	experience,	currentlyEmployee,	managedOthers,	managedHowMany]])
# 		predictValues=dct.predict(testKr)
#         
# 		testKr1 = v.transform([major])
# 		
# 		predictValues1= ann.predict(testKr1)
#         
# 		print(predictValues1) 
#         
# 		data =pd.read_csv("UserClusters.tsv", sep='\t')
# 		#q = data.iloc[len(data)]
# 		#q = q['UserID']
# 		user_id = data.UserID[len(data)-1]+1
#         #len(data) -1
# 		data.loc[len(data)] = [len(data),	user_id,	1,	0, city,state,	country, 1234, degreeType,	1,	experience,	currentlyEmployee,managedOthers	,	managedHowMany,	predictValues1[0],	predictValues[0],	predictValues1[0]+ predictValues[0]*30]
# 		data.to_csv("UserClusters.tsv", sep ='\t', index = False)
# 		global users
# 		users = pd.read_csv('UserClusters.tsv', sep='\t')
#         
# 		#user_id = 7928
# 		jobs1 = get_recommended_jobs(user_id)
#         
# 		data = jobs1.values.tolist()
# 		return render_template('index.html',  data=data)
# 
# 
# 		#return render_template('index.html')
# 	else:
# 		return render_template('index.html')
#     
# 
# 
# =============================================================================
user_id = 44025
jobs1 = get_recommended_jobs(user_id)
#df=pd.DataFrame(jobs1,columns=['Name','Age','Height','Weight'])
#desc=df.describe(include='all')
#return render_template("data_frame_analysis.html",  data_frame=df.to_html(), stat=desc.to_html())


@app.route("/")
def index():
    data = jobs1.values.tolist()
    return render_template('index.html',  data=data)
 
    
@app.route("/about")
def about():
	return render_template('about.html')


@app.route("/contact")
def contact():
	return render_template('contact.html')


@app.route("/profile")
def profile():
	return render_template('profile.html')


#@app.route("/jobDetails")
#def jobDetails():
 #   jobID = request.args.get('id')
  # 
   # return render_template('jobDetails.html',jobID=jobID)



@app.route("/ranking")
def ranking():
    jobID = int(request.args.get('id'))
    jobID_pass = [jobID]
    job_details = find_jobs_details(jobID_pass)
    job_details = job_details.reset_index(drop=True)
    #print(job_details)
    required_job = job_details.iloc[0]
    
    #print(required_job)
    required_job = required_job.values.tolist()
    #print(required_job)
    
    return render_template('jobDetails.html',jobID=required_job,op=0)




@app.route("/jobDetails")
def jobDetails():
    jobID = int(request.args.get('id'))
    jobID_pass = [jobID]
    job_details = find_jobs_details(jobID_pass)
    job_details = job_details.reset_index(drop=True)
    #print(job_details)
    required_job = job_details.iloc[0]
    
    #print(required_job)
    required_job = required_job.values.tolist()
    #print(required_job)
    
    return render_template('jobDetails.html',jobID=required_job,op=1)



@app.route("/login")
def login():
	return render_template('login.html')


@app.route("/signUp")
def signUp():
	return render_template('signup.html')

@app.route("/loginTest", methods=['POST','GET'])
def loginTest():
	if request.method=='POST':
		userID=request.form['userID']
		password=request.form['password']
		return render_template('signup.html')
           


@app.route("/postJob", methods=['POST','GET'])
def postJob():
	if request.method=='POST':
		name=request.form['name']
		description=request.form['description']
		requirements=request.form['requirements']
		startDate=request.form['startDate']
		endDate=request.form['endDate']
		location=request.form['location']
        
        
        
		feature = name + ' '+ description +' '+ requirements
		
        
        
		testKr1 = v_job.transform([feature])
		
		predictValues1Job= ann_job.predict(testKr1)
        

		data =pd.read_csv("JobsClusters.tsv", sep='\t')
		job_id = data.JobID[len(data)-1]+1
		data.loc[len(data)] = [len(data),	job_id,	1,	name, description,requirements,location,'AZ',	'US', 1234, '6/3/2019','6/3/2019',	predictValues1Job[0],0,predictValues1Job[0]]
		data.to_csv("JobsClusters1.tsv", sep ='\t', index = False)
		return render_template('index.html')
	else:
		return render_template('index.html')

@app.route("/register", methods=['POST','GET'])
def register():
	if request.method=='POST':
		name=request.form['name']
		email=request.form['email']
		password=request.form['password']

		city = request.form['city']
		state = request.form['state']		
		country = request.form['country']

		degreeType=request.form['degreeType']
		major=request.form['major']
		
		completionDate=request.form['completionDate']
		jobTitle = request.form['jobTitle']
		experience = request.form['experience']
		
		currentlyEmployee=request.form['currentlyEmployee']
		managedOthers=request.form['managedOthers']
		managedHowMany=request.form['managedHowMany']


		if (degreeType == 'None'):
		    degreeType = 0
		elif (degreeType == "Bachelor's"):
		    degreeType = 4 
		elif (degreeType == "Associate's"):
		    degreeType = 3 
		elif (degreeType == "Masters's"):
		    degreeType = 5 
		elif (degreeType == 'High School'):
		    degreeType = 1 
		elif (degreeType == 'Vocational'):
		    degreeType = 2 
		elif (degreeType == 'PhD'):
		    degreeType = 6 
		else:
		    degreeType = 1
		testKr = pd.DataFrame([[ degreeType,	1,	experience,	currentlyEmployee,	managedOthers,	managedHowMany]])
		predictValues=dct.predict(testKr)
        
		testKr1 = v.transform([major])
		
		predictValues1= ann.predict(testKr1)
        
		print(predictValues1) 
        
		data =pd.read_csv("UserClusters.tsv", sep='\t')
		user_id = data.UserID[len(data)-1]+1
		data.loc[len(data)] = [len(data),	user_id,	1,	0, city,state,	country, 1234, degreeType,	1,	experience,	currentlyEmployee,managedOthers	,	managedHowMany,	predictValues1[0],	predictValues[0],	predictValues1[0]+ predictValues[0]*30]
		data.to_csv("UserClusters.tsv", sep ='\t', index = False)
		global users
		users = pd.read_csv('UserClusters.tsv', sep='\t')
        
		jobs1 = get_recommended_jobs(user_id)
        
		data = jobs1.values.tolist()
		return render_template('index.html',  data=data)
	else:
		return render_template('index.html')
    

  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)
    

