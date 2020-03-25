from flask import Flask, request, redirect, url_for, render_template, redirect
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

from database import *	

from datetime import datetime
from flask_login import logout_user

#add_user("yuvaly", "yuvaly", "da48b686-223a-4d6d-88ae-b24f483f5c8f.jpg", "01-13-2003", "male")
#update_followers("yuvaly", "yuvalt")



print("worked")

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('loginbyyuval.html')
	else:
		user = get_user(str(request.form['username']))
		if user != None and user.password_hash == request.form["password"]:
			login_session['name'] = user.username
			user = get_user(login_session['name'])
			following = user.following.split(" ")
			all_posts = []
			for i in following:
				list_of_posts_by_user = get_post(i)
				all_posts += list_of_posts_by_user

			all_posts.sort(key =  lambda x:datetime.strptime(x.time_upload, '%Y-%m-%d %H:%M:%S.%f'))
			all_posts[::-1]
			return render_template("home.html", user = user, posts = all_posts)
        	

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('singupbyyuval.html')
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
		user = get_user(name1)

		   
		return render_template('login.html', userpic = f.filename, user = user)





@app.route('/',methods=['GET', 'POST'])
def homepage():
	#current_time = datetime.now()
		# post_list = [a, b, c]
		# lambda x: x+1
		# def func(x):
		# 	return x+1
		# post_list.sort(key =  lambda x:x.time_upload)

	print("worked")
	if request.method == 'GET':
		if 'name' in login_session:  #to display user picture  login_session['name'] != None
			user = get_user(login_session['name'])
			print(login_session['name'])
			following = user.following.split(" ")
			all_posts = []
			for i in following:
				list_of_posts_by_user = get_post(i)
				all_posts += list_of_posts_by_user

			all_posts.sort(key =  lambda x:datetime.strptime(x.time_upload, '%Y-%m-%d %H:%M:%S.%f'))
			all_posts[::-1]
			return render_template("home.html", user = user, posts = all_posts)


		else:
			posts1 = get_all_posts()
			posts1[::-1]
			return render_template("home.html", userpic = "picturiuse/avatarpro.png", posts = posts1, user = 'Guest')
		
	else:
		current_time = datetime.now()
		time_str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
		print(time_str)
		des = request.form['description']
		pic = request.files['picturebyuser']
		pic.save("static/postpics/"+pic.filename)
		name = request.form['username']
		userp = get_user(name).picture

		add_post(name, des, pic.filename, current_time, userp)
		print(name + " was created")
		return redirect(url_for('homepage')) 


@app.route('/allposts',methods=['GET', 'POST'])
def allposts():
	#current_time = datetime.now()
		# post_list = [a, b, c]
		# lambda x: x+1
		# def func(x):
		# 	return x+1
		# post_list.sort(key =  lambda x:x.time_upload)


	if request.method == 'GET':
			posts1 = get_all_posts()
			posts1[::-1]
			return render_template("allposts.html", userpic = "picturiuse/avatarpro.png", posts = posts1, user = 'Guest')
		
		

		

@app.route('/about',methods=['GET'])
def Aboutus():
	
	return render_template("AboutUs.html")
			

		



@app.route('/follow',methods=['POST'])
def follow():
	myusername = request.form['myusername']
	postusername = request.form['postusername']

	update_followers(myusername, postusername)
	print("following")
	return redirect(url_for('homepage')) 



if __name__ == '__main__':
    app.run(debug=True)