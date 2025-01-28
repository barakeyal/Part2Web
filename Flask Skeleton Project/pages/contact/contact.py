from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager

# about blueprint definition
contact = Blueprint(
    'contact',
    __name__,
    static_folder='static',
    static_url_path='/contact',
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
contact_col = mydatabase['contacts']


# Routes
@contact.route('/contact', methods = ['GET','POST'])
def index():
    request_method = request.method
    if request.method == "POST":
        full_name = request.form['full-name']
        phone_number = request.form['phone-number']
        email = request.form['email']
        message = request.form['message']
        my_dict = {'Full_Name':full_name,'Phone_Number': phone_number, 'Email': email,'Message':message}
        contact_col.insert_one(my_dict)
        return render_template('contact.html',
            full_name = full_name,
            phone_number = phone_number,
            email = email,
            message = message)
    else:
        return render_template('contact.html')




