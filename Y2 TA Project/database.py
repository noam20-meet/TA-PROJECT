from model import Base, Users,Reviews


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db" ,connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username, password):
	user_object = Users(
	username = username,
	password = password)
	session.add(user_object)
	session.commit()

def delete_user(id):
	session.query(Users).filter_by(id = id).delete()
	session.commit()

def return_all_users():
	users = session.query(Users).all()
	return users

def return_user(id):
	user = session.query(Users).filter_by(id = id).first()
	return user


def add_review(name,allergy,review):
    new_review = Reviews(name=name,allergy=allergy,review=review)
    session.add(new_review)
    session.commit()

def get_all_reviews():
  return session.query(Reviews).all()

def delete_all_reviews():
	session.query(Reviews).delete()
	session.commit()

# delete_all_reviews()



