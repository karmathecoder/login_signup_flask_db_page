from flask import Flask,request,jsonify, render_template, make_response
from authentication import *

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/loginpage',methods=['POST','GET'])
def loginpage():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    try:
        username=request.form.get('username')
        passwd = request.form.get('password')
        fullname = login_acc(username,passwd)[0][0]
        return render_template('sucess.html', sucess_msg=f"Welcome {fullname}")
    except:
        return render_template('login.html', login_msg=f"Invalid Creds")

@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template('signup.html')

@app.route('/signupsucess',methods=['GET','POST'])
def signupsucess():
    try:
        name=request.form.get('name')
        email=request.form.get('email')
        username=request.form.get('username')
        password=request.form.get('password')
        list=[name,email,username,password]
        account_creation(list)
        return render_template('signup.html',account_created=f"Account Created")
    except:
        return render_template('signup.html',account_created=f"Error Occoured")
@app.route('/logout',methods=['GET'])
def logout():
    return render_template('login.html', login_msg=f"Logout Sucessfully")

if __name__ == '__main__':
    app.run(debug=True)