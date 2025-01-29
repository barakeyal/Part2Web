import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# get your uri from .env file
uri = os.environ.get('mongodb+srv://barakeyal100:sOcTBmPZ7lCAdBx0@web-project-cluster.uiphk.mongodb.net/')

# create cluster
cluster = MongoClient('mongodb+srv://barakeyal100:sOcTBmPZ7lCAdBx0@web-project-cluster.uiphk.mongodb.net/', server_api=ServerApi('1'))

# get all dbs and collestions that needed
mydatabase = cluster['mydatabase']

####################################### Users Cluster
user_col = mydatabase['users']

### Create users
def create_user(first_name,last_name,nickname,email,phone_number,birth_day,birth_month, birth_year):
    my_dict = {"First_Name":first_name,"Last_Name":last_name,"Nickname":nickname,"Email":email,"Phone_Number": phone_number,
            "Birth_Day":birth_day,"Birth_Month":birth_month,"Birth_Year":birth_year}
    user_col.insert_one(my_dict)
    session["Logged_in"] = True
    session["Email"] = email_in

### Log in
def sign_in(phone_number_in,email_in):
    user = user_col.findOne({Email: email_in})
    if len(user)>0 and user.Phone_Number = phone_number_in: ## If doesnt work then user[Phone_Number]
        session["Logged_in"] = True
        session["Email"] = email_in


####################################### Contacts Cluster
contact_col = mydatabase['contacts']

### Create contact
def create_contact(full_name,phone_number,email,message):
    my_dict = {'Full_Name':full_name,'Phone_Number': phone_number, 'Email': email,'Message':message}
    session["Email"] = email
    contact_col.insert_one(my_dict)



####################################### Workouts Cluster
workouts_col = mydatabase['users']

### Create users
def create_workout(training_type,training_date,training_time):
    my_dict = {"Email":session['Email'],"training_type": training_type,
        "training_date":training_date,
        "training_time":training_time}
    workouts_col.insert_one(my_dict)









