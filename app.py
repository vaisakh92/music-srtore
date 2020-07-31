from flaskext.mysql import MySQL
from flask import (Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response)
import os
from werkzeug.utils import secure_filename
import calendar
import time


mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'music_store'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/logout')
def logout():
   session.pop('username', None)
   session.pop('user_id', None)
   return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
      email_id = request.form['name']
      password = request.form['password']
      cursor = mysql.connect().cursor()
      cursor.execute("SELECT * from user where email_id='" + email_id + "' and password='" + password + "'")
      data = cursor.fetchone()
      if data is None:
        flash("Invalid Email ID or password") 
        return render_template('login.html')
      else:
         session['username'] = email_id
         
         session['user_id'] = data[0]
        
      return redirect(url_for('home'))
    else:
      return render_template('login.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
      User_name = request.form['user_name']
      Address = request.form['address']
      Phone_number = request.form['phone_number']
      Email_id = request.form['email_id']
      Password = request.form['password']
      qry = " INSERT INTO `user` ( User_name, Address, Phone_number, Email_id, Password ) values " 
      qry += "('"+User_name +"','"+Address +"','"+Phone_number +"','"+Email_id +"','"+Password +"')"
      conn = mysql.connect()
      cursor = conn.cursor()
      try:
        x = cursor.execute(qry)
        if x == 1:
            conn.commit()
            cursor.execute("SELECT * from user where email_id='" + Email_id + "' and password='" + Password + "'")
            data = cursor.fetchone()  
            session['username'] = Email_id
            session['user_id'] = data[0]
            return redirect(url_for('home'))
      except :
          flash("Email ID already registered.")
          return redirect(url_for('register')) 
    return render_template('register.html')
@app.route('/home',methods = ['POST', 'GET'])
def home():    
    return render_template('home.html')
@app.route('/add',methods = ['POST', 'GET'])
def add():
    return render_template('add.html')
@app.route('/list',methods = ['POST', 'GET'])
def _list():
    return render_template('list.html')
@app.route('/search',methods = ['POST', 'GET'])
def search():
    return render_template('search.html')
@app.route('/play',methods = ['POST', 'GET'])
def song():
    return render_template('play.html')
         
if __name__ == '__main__':
   app.secret_key = 'super secret key'
   app.debug = True
   app.run() 