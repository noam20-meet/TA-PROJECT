from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from database import *
import json ,requests
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


islogged = False
recent = []
username = ""



@app.route("/")
def start():
	return render_template("start.html")

@app.route("/home")
def home():
	reviews=get_all_reviews()
	return render_template("home.html", reviews=reviews)


@app.route("/service", methods=['GET', 'POST'])
def service():
	if request.method == 'GET':
		return render_template("services.html")
	else:
		allergyType = request.form['allergyType']
		area = request.form['area']
		YOUR_API_KEY="1449d4b93a224b33b57fc8edae5f0663"
		
		TelAviv= "https://api.breezometer.com/pollen/v2/forecast/daily?lat=32.109333&lon=34.855499&days=3&key=1449d4b93a224b33b57fc8edae5f0663&features=types_information"
		
		Jerusalem="https://api.breezometer.com/pollen/v2/forecast/daily?lat=32.794044&lon=34.989571&days=3&key=1449d4b93a224b33b57fc8edae5f0663&features=types_information"
		
		Haifa="https://api.breezometer.com/pollen/v2/forecast/daily?lat=32.109333&lon=34.855499&days=3&key=1449d4b93a224b33b57fc8edae5f0663&features=types_information"
		
		BeerSheva="https://api.breezometer.com/pollen/v2/forecast/daily?lat=32.109333&lon=34.855499&days=3&key=1449d4b93a224b33b57fc8edae5f0663&features=types_information"


		if area == "telaviv" :
			response=requests.get(TelAviv)
			parsed_content = json.loads(response.content)
			data= parsed_content["data"]
			dates= [[data[0]["date"]], data[0]["types"]], [[data[1]["date"]], data[1]["types"]], [[data[2]["date"]], data[2]["types"]]
			return render_template ("services.html", dates=dates)
		elif area == "jerusalem":
			response=requests.get(Jerusalem)
			parsed_content = json.loads(response.content)
			data= parsed_content["data"]
			dates= [[data[0]["date"]], data[0]["types"]], [[data[1]["date"]], data[1]["types"]], [[data[2]["date"]], data[2]["types"]]
			return render_template ("services.html", dates=dates)
			
		elif area =="haifa":
			response=requests.get(Haifa)
			parsed_content = json.loads(response.content)
			data= parsed_content["data"]
			dates= [[data[0]["date"]], data[0]["types"]], [[data[1]["date"]], data[1]["types"]], [[data[2]["date"]], data[2]["types"]]
			return render_template ("services.html", dates=dates)
		else:
			response=requests.get(BeerSheva)
			parsed_content = json.loads(response.content)
			data= parsed_content["data"]
			dates= [[data[0]["date"]], data[0]["types"]], [[data[1]["date"]], data[1]["types"]], [[data[2]["date"]], data[2]["types"]]
			return render_template ("services.html", dates=dates)
	return render_template("services.html")
		

@app.route("/info")
def info():
	return render_template("info.html")

@app.route("/reviews", methods=['GET', 'POST'])
def reviews():
	if request.method == 'GET':
		return render_template("reviews.html")
	else:
		name = request.form['name']
		allergy = request.form['allergy']
		review = request.form['review']
		add_review(name,allergy,review)
		return render_template('home.html')


@app.route('/login' , methods = ['GET', 'POST'])
def login():
	global username
	wrong_username = ""
	wrong_password = ""
	

	if request.method == 'POST': 
		username = request.form["username"]
		password = request.form["password"]
		all_users_list = return_all_users()

		for user in all_users_list: 
			if user.username == username and user.password == password:
				return render_template("home.html", username = username)
				
			if user.username == username and user.password != password:
				wrong_password = "The password is wrong. Maybe try again!"
				return render_template("login.html", wrong_password = wrong_password,
					wrong_username = wrong_username)


			elif user.username != username and user.password == password:
				wrong_username = "The username is wrong. Maybe try again!"
				return render_template("login.html", wrong_password = wrong_password,
					wrong_username= wrong_username)

		


	return render_template("login.html")


@app.route('/signup' ,  methods = ['GET', 'POST'])
def signup():
	username_message = ""
	password_message = ""

	if request.method == 'POST':
		new_username = request.form["new_username"] 
		new_password = request.form["new_password"]
		all_users_list = return_all_users()

		for user in all_users_list: 
			if user.username == new_username and user.password == new_password:
				username_message = "This username is already in use!"
				password_message = "This password is already in use!"
				return render_template("signup.html", username_message = username_message, 
				password_message = password_message)

			elif user.username == new_username:
				username_message = "This username is already in use!"
				return render_template("signup.html", username_message = username_message, 
				password_message = password_message)

			elif user.password == new_password:
				password_message = "This password is already in use!"
				return render_template("signup.html", username_message = username_message, 
				password_message = password_message)

		add_user(new_username, new_password) 

		username_message = "You are now signed up. You can log in!"
		return render_template("login.html", username_message = username_message, 
		password_message = password_message)

	return render_template("signup.html", username_message = username_message, 
		password_message = password_message)







if __name__ == '__main__':
	app.run(debug=True)

