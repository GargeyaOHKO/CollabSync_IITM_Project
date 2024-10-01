from flask import Flask, render_template, request, redirect, url_for, flash,session
from models import Completedcampaign, Requests, db,Influencer,Company,Admin,Campaign,Ad,Ongoingcampaign
from app import app 
from werkzeug.security import generate_password_hash,check_password_hash

#url_for('static', filename='style.css')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adminlogin')
def adminlogin():
    ad=Admin.query.all()
    if not ad:
        password_hash=generate_password_hash('1234567')
        new_user = Admin(username="Admin", passhash=password_hash)
        db.session.add(new_user)
        db.session.commit()
    return render_template('adminlogin.html')

@app.route('/adminlogin' , methods=["POST"])
def adminlogin_post():
    username=request.form.get('username')
    password=request.form.get('password')
    if not username or not password:
        flash("Please fill out all the fields")
        return redirect(url_for('adminlogin'))
    user1=Admin.query.filter_by(username=username).first()
    if not user1:
        flash('Username Does Not Exist')
        return redirect(url_for('adminlogin'))
    if user1:
        if not check_password_hash(user1.passhash,password):
            flash('Incorrect Password')
            return redirect(url_for('adminlogin'))
        else:
            session['user_id']=user1.id
            return redirect(url_for('adminhome'))
        
@app.route('/adminprofile')
def adminprofile():
    if 'user_id' in session:
        return render_template('adminprofile.html')
    else:
        flash("Please Login First")
        return redirect(url_for('adminlogin'))
        
@app.route('/adminhome')
def adminhome():
    if 'user_id' in session:
        influ=Influencer.query.all()
        return render_template('adminhome.html', influ=influ)
    else:
        flash("Please Enter Correct Details")
        return redirect(url_for('adminlogin'))
    
@app.route('/admin/<int:id>/idelete')
def idelete_admin(id):
    if 'user_id' in session:
        influencer=Influencer.query.get(id)
        return render_template('admin/idelete.html',influencer=influencer)
    else:
        flash("Please Login To Continue")
        return redirect(url_for('adminlogin'))

@app.route('/admin/<int:id>/idelete',methods=['POST'])
def idelete_admin_post(id):
    influencer=Influencer.query.get(id)
    if not influencer:
        flash("Influencer Does Not Exist")
        return redirect(url_for('adminhome'))
    db.session.delete(influencer)
    db.session.commit()
    flash('Campaign Edited Successfully')
    return redirect(url_for('adminhome'))
    
@app.route('/admincampaigns')
def admincampaigns():
    if 'user_id' in session:
        campaign=Campaign.query.all()
        return render_template('admincampaigns.html',campaign=campaign)
    else:
        flash("Please Enter Correct Details")
        return redirect(url_for('adminlogin'))
    
@app.route('/admin/<int:id>/cdelete')
def cdelete_admin(id):
    if 'user_id' in session:
        campaign=Campaign.query.get(id)
        return render_template('admin/cdelete.html',campaign=campaign)
    else:
        flash("Please Login To Continue")
        return redirect(url_for('adminlogin'))

@app.route('/admin/<int:id>/cdelete',methods=['POST'])
def cdelete_admin_post(id):
    campaign=Campaign.query.get(id)
    if not campaign:
        flash("Campaign Does Not Exist")
        return redirect(url_for('admincampaigns'))
    db.session.delete(campaign)
    db.session.commit()
    flash('Campaign Edited Successfully')
    return redirect(url_for('admincampaigns'))

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
        influencer_id = session['user_id']
        applied_campaign_ids = [request.campaign_id for request in Requests.query.filter_by(influencer_id=influencer_id).all()]
        campaign = Campaign.query.filter(~Campaign.id.in_(applied_campaign_ids)).all()
        return render_template('influencerhome.html', campaign=campaign)
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
        parameter=request.args.get('parameter')
        query=request.args.get('query')
        campaign=Campaign.query.all()
        if parameter=='name':
            campaign=Campaign.query.filter(Campaign.name.ilike(f'%{query}%')).all()
            return render_template('influencerfind.html',campaign=campaign)
        elif parameter=='companyname':
            campaign=Campaign.query.filter(Campaign.companyname.ilike(f'%{query}%')).all()
            return render_template('influencerfind.html',campaign=campaign)
        elif parameter=='budget':
            campaign=Campaign.query.filter(Campaign.budget.ilike(f'%{query}%')).all()
            return render_template('influencerfind.html',campaign=campaign)
        campaign=Campaign.query.all()
        return render_template('influencerfind.html',campaign=campaign)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/influencercampaigns')
def influencercampaigns():
    if 'user_id' in session:
        user=Influencer.query.get(session['user_id'])
        influencer_id = user.id
        request=Ongoingcampaign.query.filter_by(influencer_id=influencer_id).all()
        return render_template('influencercampaigns.html',request=request)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    

@app.route('/campaign_complete/<int:request_id>', methods=['POST'])
def campaign_complete(request_id):
    campaign = Ongoingcampaign.query.get(request_id)
    if not campaign:
        flash('Campaign does not exist')
        return redirect(url_for('influencerhome'))
    influencer_id = session['user_id']
    influencer = Influencer.query.get(influencer_id)
    done = Completedcampaign(
        influencer_id=campaign.influencer_id, 
        campaign_id=campaign.campaign_id,
        company_id=campaign.company_id,
        companyname=campaign.companyname,
        request_id=campaign.request_id,
        campaigndescription=campaign.campaigndescription,
        campaignbudget=campaign.campaignbudget,
        campaignname=campaign.campaignname,
        influencername=campaign.influencername,
        influencerusername=campaign.influencerusername,
        influencercategory=campaign.influencercategory,
        influencerplatform=campaign.influencerplatform,
        influencerfollowers=campaign.influencerfollowers
    )
    db.session.add(done)
    db.session.commit()
    flash("Campaign Completed")
    request = Ongoingcampaign.query.get(request_id)
    db.session.delete(request)
    db.session.commit()
    return redirect(url_for('influencerhome'))
    
@app.route('/influencercompletedcampaigns')
def influencercompletedcampaigns():
    if 'user_id' in session:
        user=Influencer.query.get(session['user_id'])
        influencer_id = user.id
        request=Completedcampaign.query.filter_by(influencer_id=influencer_id).all()
        return render_template('influencercompletedcampaigns.html',request=request)
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
@app.route('/companycompletedcampaigns')
def companycompletedcampaigns():
    if 'user_id' in session:
        company = Company.query.get(session['user_id'])
        company_id = company.id
        request = Completedcampaign.query.filter_by(company_id=company_id).all()
        return render_template('companycompletedcampaigns.html',request=request)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))


@app.route('/companyongoingcampaigns')
def companyongoingcampaigns():
    if 'user_id' in session:
        company = Company.query.get(session['user_id'])
        companyname = company.companyname
        request = Ongoingcampaign.query.filter_by(companyname=companyname).all()
        return render_template('companyongoingcampaigns.html',request=request)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    
@app.route('/campaignrequests')
def campaignrequests():
    if 'user_id' in session:
        company_id = Company.query.get(session['user_id'])
        companyname = company_id.companyname
        request = Requests.query.filter_by(companyname=companyname).all()
        return render_template('campaignrequests.html',company_id=company_id,request=request)
    else:
        flash('Please login to continue')
        return redirect(url_for('login'))
    

@app.route('/campaignrequestsapply/<int:campaign_id>', methods=['POST'])
def campaignrequestsapply(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if not campaign:
        flash('Campaign does not exist')
        return redirect(url_for('influencerhome'))
    influencer_id = session['user_id']
    influencer = Influencer.query.get(influencer_id)
    # Check if the influencer has already applied
    existing_application = Requests.query.filter_by(influencer_id=influencer_id, campaign_id=campaign_id).first()
    if existing_application:
        flash("You have already applied for this campaign")
        return redirect(url_for('influencerhome'))
    apply = Requests(
        influencer_id=influencer_id, 
        campaign_id=campaign_id,
        companyname=campaign.companyname,
        campaigndescription=campaign.description,
        campaignbudget=campaign.budget,
        campaignname=campaign.name,
        influencername=influencer.name,
        influencerusername=influencer.username,
        influencercategory=influencer.category,
        influencerplatform=influencer.platform,
        influencerfollowers=influencer.followers
    )
    db.session.add(apply)
    db.session.commit()
    flash("Applied Successfully")
    return redirect(url_for('influencerhome'))

#Accept/Reject

@app.route('/campaignrequests_accept/<int:request_id>', methods=['POST'])
def campaignrequests_accept(request_id):
    request = Requests.query.get(request_id)
    if not request:
        flash('Request does not exist')
        return redirect(url_for('campaignrequests'))
    company=Company.query.get(session['user_id'])
    
    apply = Ongoingcampaign(
        influencer_id=request.influencer_id, 
        campaign_id=request.campaign_id,
        company_id=company.id,
        request_id=request.id,
        companyname=request.companyname,
        campaigndescription=request.campaigndescription,
        campaignbudget=request.campaignbudget,
        campaignname=request.campaignname,
        influencername=request.influencername,
        influencerusername=request.influencerusername,
        influencercategory=request.influencercategory,
        influencerplatform=request.influencerplatform,
        influencerfollowers=request.influencerfollowers
    )
    db.session.add(apply)
    db.session.commit()
    request = Requests.query.get(request_id)
    db.session.delete(request)
    db.session.commit()
    flash("Accepted Request Successfully")
    return redirect(url_for('campaignrequests'))


@app.route('/campaignrequests_reject/<int:request_id>', methods=['POST'])
def campaignrequests_reject(request_id):
    request = Requests.query.get(request_id)
    if not request:
        flash('Request does not exist')
        return redirect(url_for('campaignrequests'))
    db.session.delete(request)
    db.session.commit()
    flash('Request Rejected Successfully')
    return redirect(url_for('campaignrequests'))


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
        parameter=request.args.get('parameter')
        query=request.args.get('query')
        influ=Influencer.query.all()
        if parameter=='name':
            influ=Influencer.query.filter(Influencer.name.ilike(f'%{query}%')).all()
            return render_template('companyfind.html',influ=influ)
        elif parameter=='category':
            influ=Influencer.query.filter(Influencer.category.ilike(f'%{query}%')).all()
            return render_template('companyfind.html',influ=influ)
        elif parameter=='platform':
            influ=Influencer.query.filter(Influencer.platform.ilike(f'%{query}%')).all()
            return render_template('companyfind.html',influ=influ)
        elif parameter=='followers':
            influ=Influencer.query.filter(Influencer.followers.ilike(f'%{query}%')).all()
            return render_template('companyfind.html',influ=influ)
        influ=Influencer.query.all()
        return render_template('companyfind.html',influ=influ)
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
    flash('Campaign Added Successfully')
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
    flash('Campaign Edited Successfully')
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
    flash('Campaign Deleted Successfully')
    return redirect(url_for('companycampaigns'))