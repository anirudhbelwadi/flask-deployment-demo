#Import required methods from flask framework
from flask import Flask, request, render_template, redirect, session, url_for

#Import timedelta method from datetime module
from datetime import timedelta

#Initilize a Flask application
app = Flask(__name__)

#Use secrect key to enable session
app.secret_key = "flask auth"

#Set lifetime/timer for login session. After 1 hour, the user will be logged out
app.permanent_session_lifetime = timedelta(hours=1)

#Root Route
#Allow POST and GET methods as both will be required.
@app.route('/',methods=['POST','GET'])
def home():
    #Check if user is trying to log in
    if request.method == "POST":
        #Accept login form details 
        email = request.form['email']
        password = request.form['password']
        
        #Username and Password authentication
        if email == "anirudh@gmail.com" and password == "abcdef":
            return render_template('index.html',username=email)
        return redirect(url_for('login'))
    else:
        #Check if user is logged into the session
        if "username" in session:
            return render_template('index.html',username=session['username'])
        
        #User not logged into the session
        return redirect(url_for('login'))

#Login Route
@app.route('/login')
def login():
    #Check if user is logged into the session
    if "username" in session:
        return redirect(url_for('home'))
    
    #User not logged into the session
    return render_template('login.html')

#Logout route
@app.route('/logout')
def logout():
    #Check if user is logged into the session
    if "username" in session:
        #Remove user from session
        session.pop("username",None)
        
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)