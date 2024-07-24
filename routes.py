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
    if user1:
        if not check_password_hash(user1.passhash,password):
            flash('Incorrect Password')
            return redirect(url_for('login'))
        else:
            session['user_id']=user1.id
            return redirect(url_for('companyhome'))
    if user2:
        if not check_password_hash(user2.passhash,password):
            flash('Incorrect Password')
            return redirect(url_for('login'))
        else:
            session['user_id']=user2.id
            return redirect(url_for('influencerhome'))

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
    if len(password)<7:
        flash('Password should be atleast 7 characters long')
        return redirect(url_for('influencerregister'))
    user1=Influencer.query.filter_by(username=username).first()
    user2=Company.query.filter_by(username=username).first()
    if user1 or user2:
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
        return redirect(url_for('companyregister'))
    user1=Company.query.filter_by(username=username).first()
    user2=Influencer.query.filter_by(username=username).first()
    if user1 or user2:
        flash("Username already exists")
        return redirect(url_for('companyregister'))
    password_hash=generate_password_hash(password)
    new_user=Company(companyname=companyname,passhash=password_hash,username=username,industry=industry,budget=budget)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('login'))


#influencer


@app.route('/influencerhome')
def influencerhome():
    if 'user_id' in session:
        campaign=Campaign.query.all()
        return render_template('influencerhome.html',campaign=campaign)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/influencerprofile')
def influencerprofile():
    if 'user_id' in session:
        user=Influencer.query.get(session['user_id'])
        return render_template('influencerprofile.html',user=user)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/influencerfind')
def influencerfind():
    if 'user_id' in session:
        return render_template('influencerfind.html')
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/influencercampaigns')
def influencercampaigns():
    if 'user_id' in session:
        return render_template('influencercampaigns.html')
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/influencerprofileedit')
def influencerprofileedit():
    if 'user_id' in session:
        return render_template('influencerprofileedit.html')
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/influencerprofileedit',methods=['POST'])
def influencerprofileedit_post():
    name=request.form.get('name')
    oldpassword=request.form.get('oldpassword')
    newpassword=request.form.get('newpassword')
    followers=request.form.get('followers')
    platform=request.form.get('platform')
    
    if not oldpassword:
        flash('Please Enter Your Password to Make Changes')
        return redirect(url_for('influencerprofileedit'))
    user=Influencer.query.get(session['user_id'])
    if not check_password_hash(user.passhash,oldpassword):
        flash('Incorrect Password')
        return redirect(url_for('influencerprofileedit'))
    if newpassword:
        newpasswordhash=generate_password_hash(newpassword)
    if name:
        user.name=name
    if newpassword:
        user.passhash=newpasswordhash
    if followers:
        user.followers=followers
    if platform:
        user.platform=platform
    db.session.commit()
    return redirect(url_for('influencerprofile'))
    

#company


@app.route('/companyhome')
def companyhome():
    if 'user_id' in session:
        campaigns = Campaign.query.all()
        return render_template('companyhome.html', campaigns=campaigns)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))

@app.route('/companyprofile')
def companyprofile():
    if 'user_id' in session:
        user=Company.query.get(session['user_id'])
        return render_template('companyprofile.html',user=user)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/companyfind')
def companyfind():
    if 'user_id' in session:
        return render_template('companyfind.html')
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))

@app.route('/companycampaigns')
def companycampaigns():
    if 'user_id' in session:
        company = Company.query.get(session['user_id'])
        companyname = company.companyname
        campaigns = Campaign.query.filter_by(companyname=companyname).all()
        return render_template('companycampaigns.html', campaigns=campaigns,company=company)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/companyprofileedit')
def companyprofileedit():
    if 'user_id' in session:
        return render_template('companyprofileedit.html')
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))

@app.route('/companyprofileedit',methods=['POST'])
def companyprofileedit_post():
    companyname=request.form.get('companyname')
    oldpassword=request.form.get('oldpassword')
    newpassword=request.form.get('newpassword')
    industry=request.form.get('industry')
    budget=request.form.get('budget')
    
    if not oldpassword:
        flash('Please Enter Your Password to Make Changes')
        return redirect(url_for('companyprofileedit'))
    user=Company.query.get(session['user_id'])
    if not check_password_hash(user.passhash,oldpassword):
        flash('Incorrect Password')
        return redirect(url_for('companyprofileedit'))
    if newpassword:
        newpasswordhash=generate_password_hash(newpassword)
    if companyname:
        user.companyname=companyname
    if newpassword:
        user.passhash=newpasswordhash
    if budget:
        user.budget=budget
    if industry:
        user.industry=industry
    db.session.commit()
    return redirect(url_for('companyprofile'))


@app.route('/campaign/add')
def add_campaign():
    if 'user_id' in session:
        return render_template('campaign/add.html')
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))

@app.route('/campaign/add',methods=['POST'])
def add_campaign_post():
    name=request.form.get('name')
    description=request.form.get('description')
    budget=request.form.get('budget')
    company = Company.query.get(session['user_id'])
    companyname = company.companyname
    if not name or not description or not budget:
        flash("Please Fill Out All The Fields")
        return redirect(url_for('add_campaign'))
    campaign=Campaign(companyname=companyname,name=name,description=description,budget=budget,visibility=True)
    db.session.add(campaign)
    db.session.commit()
    #flash('Campaign Added Successfully')
    return redirect(url_for('companycampaigns'))
    
@app.route('/campaign/<int:id>/edit')
def edit_campaign(id):
    if 'user_id' in session:
        campaign=Campaign.query.get(id)
        if not campaign:
            flash("Campaign Does Not Exist")
            return redirect(url_for('companycampaigns'))
        return render_template('campaign/edit.html',campaign=campaign)
    else:
        flash("Please Login To Continue")
        return redirect(url_for('login'))

@app.route('/campaign/<int:id>/edit',methods=['POST'])
def edit_campaign_post(id):
    campaign=Campaign.query.get(id)
    if not campaign:
        flash("Campaign Does Not Exist")
        return redirect(url_for('companycampaigns'))
    name=request.form.get('name')
    description=request.form.get('description')
    budget=request.form.get('budget')
    campaign.name=name
    campaign.description=description
    campaign.budget=budget
    db.session.commit()
    #flash('Campaign Edited Successfully')
    return redirect(url_for('companycampaigns'))    

@app.route('/campaign/<int:id>/delete')
def delete_campaign(id):
    if 'user_id' in session:
        campaign=Campaign.query.get(id)
        return render_template('campaign/delete.html',campaign=campaign)
    else:
        flash("Please Login To Continue")
        return redirect(url_for('login'))

@app.route('/campaign/<int:id>/delete',methods=['POST'])
def delete_campaign_post(id):
    campaign=Campaign.query.get(id)
    if not campaign:
        flash("Campaign Does Not Exist")
        return redirect(url_for('companycampaigns'))
    db.session.delete(campaign)
    db.session.commit()
    #flash('Campaign Edited Successfully')
    return redirect(url_for('companycampaigns'))