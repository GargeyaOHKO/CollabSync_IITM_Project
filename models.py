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
    companyname=db.Column(db.String(32),unique=False,nullable=False)
    username=db.Column(db.String(32),unique=True,nullable=False)
    passhash=db.Column(db.String(100),unique=False,nullable=False)
    industry=db.Column(db.String(32),unique=False,nullable=False)
    budget=db.Column(db.Integer,unique=False,nullable=False)

class Admin(db.Model):
    __tablename__='admin'
    id=db.Column(db.Integer,primary_key=True)
    passhash=db.Column(db.String(100),unique=False,nullable=False)

class Campaign(db.Model):
    __tablename__='campaign'
    id=db.Column(db.Integer,primary_key=True)
    company_id=db.Column(db.Integer,db.ForeignKey('company.id'),nullable=False)
    name=db.Column(db.String(32),unique=True,nullable=False)
    description=db.Column(db.String(100),unique=False,nullable=False)
    budget=db.Column(db.String(32),unique=False,nullable=False)
    visibility=db.Column(db.String(32),unique=False,nullable=False)
    goals=db.Column(db.String(100),unique=False,nullable=False)
    
class Ad(db.Model):
    __tablename__='ad'
    id=db.Column(db.Integer,primary_key=True)
    campaign_id=db.Column(db.Integer,db.ForeignKey('campaign.id'),nullable=False)
    influencer_id=db.Column(db.Integer,db.ForeignKey('influencer.id'),nullable=False)
    messages=db.Column(db.String(100),unique=True,nullable=False)
    payamt=db.Column(db.String(100),unique=False,nullable=False)
    status=db.Column(db.String(32),unique=False,nullable=False)

class Role(db.Model):
    __tablename__='role'
    role=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('influencer.id'),nullable=False)

with app.app_context():
    db.create_all()
    

