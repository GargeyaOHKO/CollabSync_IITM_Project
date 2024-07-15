from flask import Flask, render_template, request, redirect, url_for, flash
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

@app.route('/influencerregister')
def influencerregister():
    return render_template('influencerregister.html')

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
    user=Company.query.filter_by(companyname=companyname).first()
    if user:
        flash("Username already exists")
        return redirect(url_for('companyregister'))
    password_hash=generate_password_hash(password)
    new_user=Company(companyname=companyname,passhash=password_hash,username=username,industry=industry,budget=budget)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))

    
    

