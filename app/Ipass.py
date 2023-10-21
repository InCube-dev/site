from app import app
from flask import render_template
import mysql.connector
session = mysqlx.get_session(
   host="",
   user="",
   port=0,
   password="")

@app.route('/incubepass') # инкубпасс
def inpass():
    return render_template("pass.html",title="InCube Pass")