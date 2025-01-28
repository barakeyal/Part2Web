from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager
from utilities.db.db_manager import cluster



# catalog blueprint definition
catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog', template_folder='templates')

#
mydb  = cluster["trainings"]

# Routes
@catalog.route('/catalog',methods=["GET","POST"])
def index():
    request_method = request.method
    if request.method == "POST":
        training_type = request.args['training-type']
        training_date = request.args['training-date']
        training_time = request.args['training-time']
        pass
    else:
        pass

    return render_template('catalog.html',
        request_method = request_method,
        training_type = training_type,
        training_date = training_date,
        training_time = training_time)
