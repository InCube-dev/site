from app import app
from flask import render_template

@app.route('/incubepass') # инкубпасс
def inpass():
    data = {}
    return render_template("pass.html",title="InCube Pass",data=data)