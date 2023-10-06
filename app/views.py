from app import app
from flask import render_template
import auth

@app.route('/') # Главная
def index():
    return render_template("index.html")

@app.route('/discords') # дискорд сервера
def index():
    return render_template("discords.html")

@app.route('/options') # настройки
def index():
    return render_template("options.html")

@app.route('/profile') # профиль
def index():
    return render_template("profiles.html")

@app.route('/wiki') # вики
def index():
    return render_template("wiki.html")

@app.route('/content') # видео/стримы
def index():
    return render_template("contents.html")

@app.route('/buy') # покупка
def index():
    return render_template("buy.html")

@app.route('/incubepass') # инкубпасс
def index():
    return render_template("incubepass.html")