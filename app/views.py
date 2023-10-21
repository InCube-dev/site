from app import app
from flask import render_template

@app.route('/') # Главная
def index():
    return render_template("index.html")

@app.route('/discords') # дискорд сервера
def discords():
    return render_template("discords.html",title="Дисорды")

@app.route('/options') # настройки
def options():
    return render_template("options.html",title="Настройки")

@app.route('/profile') # профиль
def profile():
    return render_template("profiles.html",title="Профиль")

@app.route('/content') # видео/стримы
def content():
    return render_template("contents.html",title="Контент")

@app.route('/buy') # покупка
def buy():
    return render_template("buy.html",title="Покупка")
