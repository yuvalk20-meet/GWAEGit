from model import Base, User, Posts


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

'''
def add_user(name, secret_word, pic, bir, gen):
    user_object = User(username=name)
    user_object.password_hash(secret_word)
    user_object.picture(pic)
    user_object.birthday(bir)
    user_object.gender(gen)
    user_object.followers("")
    user_object.following("")
    
    session.add(user_object)
    session.commit()
'''
def add_user(name, secret_word, pic, bir, gen):
    user = User(username=name, password_hash = secret_word, picture = pic, birthday = bir, gender = gen, followers = "", following = "")
    session.add(user)
    session.commit()

def add_post(name, des, pic, time):
    post = Posts(username=name, description = des, picture = pic, time_upload = time)
    session.add(post)
    session.commit()

def get_post(Username):
  return session.query(Posts).filter(username=Username).all()

def get_user(Username):
  return session.query(User).filter(username=Username).first()

def get_all_posts():
  return session.query(Posts).all()

def update_followers(username, new_following):
   """
   Update a student in the database, with
   whether or not they have finished the lab
   """
   post_object = session.query(
       Posts).filter_by(
       username=username).first()
   post_object.following += " " + new_following
   session.commit()
