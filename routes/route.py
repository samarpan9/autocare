import flask
from flask import session , flash
from flask.templating import render_template 
from flask.globals import request
from datetime import timedelta
from functools import wraps
from werkzeug.utils import redirect
import hashlib
from web_app import app, db
from core.queries import get_garage_info, get_garages_list, get_services_list, get_subscription_packages,get_search_list, get_user_sub, get_user_bookings, get_user_services

#Internal file import
from web_app import app
from models.model import  User, Booking, Subscription

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#login_required
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'current_user' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect('/login')
    return wrap

# login, method=GET
@app.route("/login")
def users_get():
    return flask.render_template("auth/login.html")

# login, method=POST
@app.route("/login", methods=['POST'])
def login():
    if request.method =='POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        hashed_password=hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = User.query.filter_by(user_name = username).first()
        if user and user.passhash == hashed_password:
            session['current_user']={
                "username": user.user_name,
                "user_id": int(user.user_id)
                }
            return redirect("/")
    return render_template('auth/login.html', message="Invalid Credentials")

#logout
@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect('/login')

# signup, method=GET
@app.route("/signup")
def signup_get():
    return flask.render_template("auth/signup.html")


# signup, method=POST
@app.route("/signup", methods=['POST'])
def signup_post():
    if request.method =='POST':
        username = flask.request.form['user_name']
        password = flask.request.form['password']
        phone_number = flask.request.form['phone_number']
        hashed_password=hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        data = {
        'user_name' : username,
        'phone_number' : phone_number,
        'passhash' : hashed_password,
        }
        
        support  = User(**data)
        db.session.add(support)
        db.session.commit()

    return render_template('auth/login.html')


#dashboard
@app.route("/")
@app.route("/homepage")
def homepage():
    services_list = get_services_list()
    garages_data = get_garages_list()
    return flask.render_template("garage_dashboard.html",garage_data = garages_data, services_list =services_list)

@app.route("/homepage", methods=['POST'])
def homepage_post():
    search_item = flask.request.form['search_item']
    garages_data = get_search_list(search_item)
    
    return flask.render_template("ui/garage-list.html",garage_data =garages_data)


@app.route("/about-us")
def about_us():
    return flask.render_template("ui/about-us.html")

@app.route("/contact")
def contact_page():
    return flask.render_template("ui/contact.html")

@app.route("/garages")
def garage_list():
    garages_data = get_garages_list()
    return flask.render_template("ui/garage-list.html",garage_data = garages_data)


@app.route("/garages/<garage_id>")
def garage_details(garage_id):
    garage_info = get_garage_info(garage_id)
    return render_template('ui/details.html',garage_info = garage_info)

@app.route("/garages/book/<garage_id>")
@login_required
def garage_book_get(garage_id):
    sub_list = get_subscription_packages()
    service_list = get_services_list()
    return render_template('ui/checkout.html',service_list = service_list,garage_id = garage_id, sub_list =sub_list)

@app.route("/garages/book/<garage_id>", methods=['POST'])
@login_required
def garage_book_post(garage_id):
    user_id = request.form['user_id']
    services = request.form['services-id']
    timing = request.form['timing']
    pd_btn = request.form['hidden-pd']
    brand = request.form['brand']
    brand_model = request.form['brand_no']
    subscription = request.form['sub']
    
    if pd_btn:
        pd_bool = 'true'
        user_loc = request.form['user_loc']
        pd_data = {
            'user_loc'    : user_loc,       
        }
    else:
        pd_bool = 'false'
        
    if subscription:
        sub_duration = request.form['sub_duration']
        sub_data = {
            'user_id'       : user_id,
            'garage_id'     :  garage_id,
            'service_ids'   :  services,
            'package_id'    : sub_duration,       
        }
        print(sub_data)
        sub_dt = Subscription(**sub_data)
        db.session.add(sub_dt)
        
    data = {
        'user_id'       :  user_id,
        'garage_id'     :  garage_id,
        'service_ids'   :  services,
        'timing'        :  timing,
        'delivery'      :  pd_bool,
        'brand'         :  brand,
        'brand_model'   :  brand_model,
    }
    
    if pd_btn:
        data.update(pd_data)
    
    booking_dt  = Booking(**data)
    db.session.add(booking_dt)
    
    
    
    db.session.commit()
     
    return redirect('/profile')


@app.route("/profile")
def profile():
    user_id = session['current_user']['user_id']
    user_sub = get_user_sub(user_id)
    
    user_bookings = get_user_bookings(user_id)
    servicing_data = []
    
    test_dt = [r._asdict() for r in user_bookings]
    
    for i in test_dt:
        service_ids = i['service_ids']
        uncleaned_user_services = get_user_services(service_ids)
        user_services = {item[0] for item in uncleaned_user_services}

        i.update({'user_services' : user_services})
        servicing_data.append(i)
    current_servicing_data = servicing_data[0]
    return flask.render_template("ui/profile.html",user_sub =user_sub, servicing_data =servicing_data,current_servicing_data =current_servicing_data)





