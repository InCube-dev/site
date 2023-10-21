from app import app
from flask import render_template

@app.route('/wiki') # вики
def wiki():
    return render_template("wiki.html",title="Wiki")

@app.route('/wiki/<string:player>') # вики игрока
def wikiPlayer(player):
    wiki = {
        "nick":"",
        "about":"",
        "avatarURL":"",
        "status":""
    }
    return render_template("wikiPlayer.html",wiki=wiki,title=wiki["nick"])