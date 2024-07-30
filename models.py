from flask_sqlalchemy import SQLAlchemy
from app import app
db=SQLAlchemy(app)

class Influencer(db.Model):
    __tablename__='influencer'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),unique=True,nullable=False)
    passhash=db.Column(db.String(100),unique=False,nullable=False)
    name=db.Column(db.String(32),unique=False,nullable=False)
    category=db.Column(db.String(32),unique=False,nullable=False)
    platform=db.Column(db.String(32),unique=False,nullable=False)
    followers=db.Column(db.String(32),unique=False,nullable=False)
    earnings=db.Column(db.Integer,unique=False,nullable=True)

class Company(db.Model):
    __tablename__='company'
    id=db.Column(db.Integer,primary_key=True)
    companyname=db.Column(db.String(32),unique=True,nullable=False)
    username=db.Column(db.String(32),unique=True,nullable=False)
    passhash=db.Column(db.String(100),unique=False,nullable=False)
    industry=db.Column(db.String(32),unique=False,nullable=False)
    budget=db.Column(db.Integer,unique=False,nullable=False)

class Admin(db.Model):
    __tablename__='admin'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),unique=False,nullable=False)
    passhash=db.Column(db.String(100),unique=False,nullable=False)

class Campaign(db.Model):
    __tablename__='campaign'
    id=db.Column(db.Integer,primary_key=True)
    companyname=db.Column(db.String(32),unique=False,nullable=False)
    name=db.Column(db.String(32),unique=True,nullable=False)
    description=db.Column(db.String(100),unique=False,nullable=False)
    budget=db.Column(db.String(32),unique=False,nullable=False)
    visibility=db.Column(db.String(32),unique=False,nullable=True)

    #company = db.relationship('Company', backref=db.backref('campaigns', lazy=True))
    
class Ad(db.Model):
    __tablename__='ad'
    id=db.Column(db.Integer,primary_key=True)
    campaign_id=db.Column(db.Integer,db.ForeignKey('campaign.id'),nullable=False)
    influencer_id=db.Column(db.Integer,db.ForeignKey('influencer.id'),nullable=False)
    messages=db.Column(db.String(100),unique=True,nullable=False)
    payamt=db.Column(db.String(100),unique=False,nullable=False)
    status=db.Column(db.String(32),unique=False,nullable=False)

class Requests(db.Model):
    __tablename__='requests'
    id=db.Column(db.Integer,primary_key=True)
    influencer_id=db.Column(db.Integer,unique=False,nullable=False)
    campaign_id=db.Column(db.Integer,unique=False,nullable=False)
    campaignname=db.Column(db.String(32),unique=False,nullable=False)
    campaigndescription=db.Column(db.String(100),unique=False,nullable=False)
    campaignbudget=db.Column(db.String(32),unique=False,nullable=False)
    companyname=db.Column(db.String(32),unique=False,nullable=False)
    influencerusername=db.Column(db.String(32),unique=False,nullable=False)
    influencername=db.Column(db.String(32),unique=False,nullable=False)
    influencercategory=db.Column(db.String(32),unique=False,nullable=False)
    influencerplatform=db.Column(db.String(32),unique=False,nullable=False)
    influencerfollowers=db.Column(db.String(32),unique=False,nullable=False)

class Ongoingcampaign(db.Model):
    __tablename__='ongoingcampaign'
    id=db.Column(db.Integer,primary_key=True)
    influencer_id=db.Column(db.Integer,unique=False,nullable=False)
    campaign_id=db.Column(db.Integer,unique=False,nullable=False)
    company_id=db.Column(db.Integer,unique=False,nullable=False)
    request_id=db.Column(db.Integer,unique=False,nullable=False)
    campaignname=db.Column(db.String(32),unique=False,nullable=False)
    campaigndescription=db.Column(db.String(100),unique=False,nullable=False)
    campaignbudget=db.Column(db.String(32),unique=False,nullable=False)
    companyname=db.Column(db.String(32),unique=False,nullable=False)
    influencerusername=db.Column(db.String(32),unique=False,nullable=False)
    influencername=db.Column(db.String(32),unique=False,nullable=False)
    influencercategory=db.Column(db.String(32),unique=False,nullable=False)
    influencerplatform=db.Column(db.String(32),unique=False,nullable=False)
    influencerfollowers=db.Column(db.String(32),unique=False,nullable=False)

class Completedcampaign(db.Model):
    __tablename__='completedcampaign'
    id=db.Column(db.Integer,primary_key=True)
    influencer_id=db.Column(db.Integer,unique=False,nullable=False)
    campaign_id=db.Column(db.Integer,unique=False,nullable=False)
    company_id=db.Column(db.Integer,unique=False,nullable=False)
    request_id=db.Column(db.Integer,unique=False,nullable=False)
    campaignname=db.Column(db.String(32),unique=False,nullable=False)
    campaigndescription=db.Column(db.String(100),unique=False,nullable=False)
    campaignbudget=db.Column(db.String(32),unique=False,nullable=False)
    companyname=db.Column(db.String(32),unique=False,nullable=False)
    influencerusername=db.Column(db.String(32),unique=False,nullable=False)
    influencername=db.Column(db.String(32),unique=False,nullable=False)
    influencercategory=db.Column(db.String(32),unique=False,nullable=False)
    influencerplatform=db.Column(db.String(32),unique=False,nullable=False)
    influencerfollowers=db.Column(db.String(32),unique=False,nullable=False)


with app.app_context():
    db.create_all()
    

