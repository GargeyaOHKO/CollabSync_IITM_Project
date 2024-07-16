from flask import Flask, render_template, request, redirect, url_for, flash,session
from models import db,Influencer,Company,Admin,Campaign,Ad
from app import app 
from werkzeug.security import generate_password_hash,check_password_hash

#url_for('static', filename='style.css')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login' , methods=["POST"])
def login_post():
    username=request.form.get('username')
    password=request.form.get('password')

    if not username or not password:
        flash("Please fill out all the fields")
        return redirect(url_for('login'))
    user1=Company.query.filter_by(username=username).first()
    user2=Influencer.query.filter_by(username=username).first()
    if not user1 and not user2:
        flash('Username Does Not Exist')
        return redirect(url_for('login'))
    if not check_password_hash(user1.passhash,password) and not check_password_hash(user2.passhash,password):
        flash('Incorrect Password')
        return redirect(url_for('login'))
    if user1:
        session['user_id']=user1.id
        return redirect(url_for('companyhome'))
    elif user2:
        session['user_id']=user2.id
        return  redirect(url_for('influencerhome'))


@app.route('/influencerregister')
def influencerregister():
    return render_template('influencerregister.html')

@app.route('/influencerregister',methods=['POST'])
def influencerregister_post():
    name=request.form.get('name')
    username=request.form.get('username')
    password=request.form.get('password')
    followers=request.form.get('followers')
    category=request.form.get('category')
    platform=request.form.get('platform')

    if not name or not username or not password or not followers or not category or not platform:
        flash('Please Fill Out All Fields') 
        return redirect(url_for('influencerregister'))
    user=Influencer.query.filter_by(username=username).first()
    if user:
        flash("Username already exists")
        return redirect(url_for('influencerregister'))
    password_hash=generate_password_hash(password)
    new_user=Influencer(name=name,passhash=password_hash,username=username,followers=followers,category=category,platform=platform,earnings=0)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))



@app.route('/companyregister')
def companyregister():
    return render_template('companyregister.html')

@app.route('/companyregister',methods=['POST'])
def companyregister_post():
    companyname=request.form.get('companyname')
    username=request.form.get('username')
    password=request.form.get('password')
    industry=request.form.get('industry')
    budget=request.form.get('budget')

    if not companyname or not username or not password or not industry or not budget:
        flash('Please Fill Out All Fields') 
        return redirect(url_for('companyregister'))
    if len(password)<7:
        flash('Password should be atleast 7 characters long')
    user=Company.query.filter_by(username=username).first()
    if user:
        flash("Username already exists")
        return redirect(url_for('companyregister'))
    password_hash=generate_password_hash(password)
    new_user=Company(companyname=companyname,passhash=password_hash,username=username,industry=industry,budget=budget)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/influencerhome')
def influencerhome():
    if 'user_id' in session:
        return render_template('influencerhome')
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/companyhome')
def companyhome():
    if 'user_id' in session:
        return render_template('companyhome')
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))

