from flask import Blueprint
from flask import render_template, redirect, url_for, request
from utilities.db.db_manager import dbManager



# homepage blueprint definition
profile = Blueprint(
    'profile',
    __name__,
    static_folder='static',
    static_url_path='/profile',
    template_folder='templates'
)

import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# get your uri from .env file
uri = os.environ.get('DB_URI')

# create cluster
cluster = MongoClient('mongodb+srv://barakeyal100:sOcTBmPZ7lCAdBx0@web-project-cluster.uiphk.mongodb.net/', server_api=ServerApi('1'))

# get all dbs and collestions that needed
mydatabase = cluster['mydatabase']
user_col = mydatabase['users']


# Routes
@profile.route('/profile', methods = ['GET','POST'])
def index():
    request_method = request.method
    if request.method == "POST":
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        nickname = request.form['nickname']
        email = request.form['email']
        phone_number = request.form['phone-number']
        birth_day = request.form['day']
        birth_month = request.form['month']
        birth_year = request.form['year']
        my_dict = {"First_Name:":first_name,
            "Last_Name":last_name,
            "Nickname":nickname,
            "Email":email,
            "Phone Number": phone_number,
            "Birth_Day":birth_day,
            "Birth_Month":birth_month,
            "Birth_Year":birth_year}
        user_col.insert_one(my_dict)
        return render_template('profile.html',
            first_name = first_name,
            last_name = last_name,
            nickname = nickname,
            email = email,
            phone_number = phone_number,
            birth_day = birth_day,
            birth_month = birth_month,
            birth_year = birth_year
        ) 
    else:
        return render_template('profile.html')


