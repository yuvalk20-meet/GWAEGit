from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from passlib.apps import custom_app_context as pwd_security 
from sqlalchemy.sql import func



Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String)
	password_hash = Column(String)
	picture = Column(String)
	birthday = Column(String)
	gender = Column(String)
	followers = Column(String) #list of followers as a string   
	following = Column(String)

def hash_password(self, password):
	self.password_hash = pwd_security.encrypt(password)
def verify_password(self, password):
	return pwd_security.verify(password,self.password_hash)


class Posts(Base):
	__tablename__ = 'posts'
	id = Column(Integer, primary_key=True)
	username = Column(String)
	picture = Column(String)
	description = Column(String)
	time_upload = Column(String)
	userpic = Column(String)

