from flask import Blueprint
from flask import render_template, redirect, url_for, request
from utilities.db.db_manager import dbManager
from db_connector import create_user


# homepage blueprint definition
profile = Blueprint(
    'profile',
    __name__,
    static_folder='static',
    static_url_path='/profile',
    template_folder='templates'
)

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
        create_user(first_name,last_name,nickname,email,phone_number,birth_day,birth_month, birth_year)
        return render_template('profile.html',
            first_name = first_name,
            last_name = last_name,
            nickname = nickname,
            email = email,
            phone_number = phone_number,
            birth_day = birth_day,
            birth_month = birth_month,
            birth_year = birth_year) 
    else:
        return render_template('profile.html')


