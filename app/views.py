from app import app
from flask import render_template

@app.route('/') # Главная
def index():
    return render_template("index.html")

@app.route('/discords') # дискорд сервера
def index():
    return render_template("discords.html",title="Дисорды")

@app.route('/options') # настройки
def index():
    return render_template("options.html",title="Настройки")

@app.route('/profile') # профиль
def index():
    return render_template("profiles.html",title="Профиль")

@app.route('/wiki') # вики
def index():
    return render_template("wiki.html",title="Wiki")

@app.route('/wiki/<string:player>') # вики игрока
def index(player):
    wiki = {
        "nick":"",
        "about":"",
        "avatarURL":"",
        "status":""
    }
    return render_template("wikiPlayer.html",wiki=wiki,title=wiki["nick"])

@app.route('/content') # видео/стримы
def index():
    return render_template("contents.html",title="Контент")

@app.route('/buy') # покупка
def index():
    return render_template("buy.html",title="Покупка")

@app.route('/incubepass') # инкубпасс
def index():
    return render_template("pass.html",title="InCube Pass")
