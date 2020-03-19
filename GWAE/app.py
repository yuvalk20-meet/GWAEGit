from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

from database import *	

from datetime import datetime

print("worked")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
    	return render_template('login.html')
    else:
    	user = get_user(str(request.form['username']))
    	if user != None and user.password == request.form["password"]:
        	login_session['name'] = user.username
        	return render_template('home.html',userpic = user.picture, username = user.username)
    	else:
        	return home()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		name1 = request.form['username']
		secret_word = request.form['password']
		f = request.files['pic']     
		f.save("static/userpic/"+f.filename)
		bir = str(request.form['birthdaytime'])
		print(bir)   #
		gen = request.form['gender']
		add_user(name1, secret_word, f.filename, bir, gen)   
		print(name1 + " was created") 

		   
		return render_template('home.html', userpic = f.filename)





@app.route('/',methods=['GET', 'POST'])
def homepage():
	#current_time = datetime.now()
		# post_list = [a, b, c]
		# lambda x: x+1
		# def func(x):
		# 	return x+1
		# post_list.sort(key =  lambda x:x.time_upload)


	if request.method == 'GET':
		if 'name' in login_session:  #to display user picture  login_session['name'] != None
			user = get_user(login_session['name'])
			following = user.following.split(" ")
			all_posts = []
			for i in following:
				list_of_posts_by_user = get_post(i)
				all_posts += list_of_posts_by_user

			all_posts.sort(key =  lambda x:x.time_upload)
			return render_template("home.html", user = user, posts = all_posts)


		else:
			posts1 = get_all_posts()
			return render_template("home.html", userpic = "picturiuse/avatarpro.png", posts = posts1, user = 'Guest')
		
	else:
		current_time = datetime.now()
		des = request.form['description']
		pic = request.files['picturebyuser']
		pic.save("static/userpic/"+pic.filename)
		name = request.form['username']

		add_post(name, des, pic, current_time)
		print(name + " was created")
		return render_template("home.html")


		

		



@app.route('/follow',methods=['POST'])
def follow():
	myusername = request.form['myusername']
	postusername = request.form['postusername']

	update_followers(myusername, postusername)
	print("following")




if __name__ == '__main__':
    app.run(debug=True)