from app import app
from flask import render_template
import sqlHandler

@app.route('/incubepass') # инкубпасс
def inpass():
    return render_template("pass.html",title="InCube Pass")