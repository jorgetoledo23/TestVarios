from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from mysqlcon import *

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def main():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form.get('user')
        passw = request.form.get('passw')

        dao = DAO()
        users = dao.findUser(username)
       # print(users.count())
        if len(users) > 0:
            if users[0].password == passw:
                session["user"] = users[0].username
                session["rol"] = users[0].rol
                return render_template('home.html', user=users[0], passw=passw)
            else:
                return render_template('login.html', error="BAD CREDENTIALS")
        else:
            return render_template('login.html', error="BAD USERNAME")

    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/verusuarios')
def verusuarios():
    #Ir a la BD y leer todos los usuarios
    if (session["rol"] == 1):
        dao = DAO()
        users = dao.returnAllUsers()
        return render_template("verusuarios.html", users=users)
    else:
        return redirect("/home")

if __name__ == '__main__':
    app.run(debug=True)