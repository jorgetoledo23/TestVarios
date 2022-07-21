import mysql.connector
from mysql.connector import errorcode


class User:
    def __init__(self, userid, username, password, rol):
        self.userid = userid
        self.username = username
        self.password = password
        self.rol = rol

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user='root', password='',
                host='127.0.0.1',
                database='pywebapp')
            print('Conexion MySql Establecida Correctamente!')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    
    def findUser(self, user):
        cursor = self.cnx.cursor()
        query = ("select * from users where username = %s")
        param = (user,)
        cursor.execute(query, param)
        users = []
        for (userid, username, password, rol) in cursor:
            user = User(userid, username, password, rol)
            users.append(user)
        return users


    def returnAllUsers(self):
        cursor = self.cnx.cursor()
        query =("SELECT * FROM users")
        cursor.execute(query)
        users = []
        for (userid, username, password, rol) in cursor:
            user = User(userid, username, password, rol)
            users.append(user)
        return users
    