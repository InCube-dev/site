import sqlite3
def starts(bd: str):
    try:
        connect = sqlite3.connect(bd)

        cursor = connect.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                       id INTEGER PRIMARY KEY,
                       UUID TEXT,
                       playerName TEXT,
                       complatePass INTEGER,
                       collectedPass INTEGER,
                       paidPass INTEGER,
                       experiance INTEGER,
                       quest TEXT,
                       dateBuy TEXT,
                       forBuyEntry INTEGER
            )''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ICPass (
                       id INTEGER PRIMARY KEY,
                       rewordF INTEGER,
                       rewordP integER,
                       count INTEGER,
                       srcimg TEXT
            )''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entry (
                       idPlayer INTEGER PRIMARY KEY,
                       buyDate TEXT,
                       entryTime INTEGER
            )''')

        connect.close()
    except NameError:
        print(NameError)

def getKey(key: int, bd: str, table: str):
    try:
        connect = sqlite3.connect(bd)
        cursor = connect.cursor()
        cursor.execute(f'''
        SELECT * FROM {table} WHERE id = {key}
        ''')
        results = cursor.fetchall()
        connect.close()
        return result;
    except NameError:
        print(NameError)
def addKey(key: int, bd: str, table: str, values: dict):
    try:
        connect = sqlite3.connect(bd)
        cursor = connect.cursor()
        cursor.execute(f'''
        
        ''')
        connect.close()
        return result;
    except NameError:
        print(NameError)
def setKey(key: int, bd: str, table: str):
    try:
        connect = sqlite3.connect(bd)
        cursor = connect.cursor()
        cursor.execute(f'''
        SELECT * FROM {table} WHERE id = {key}
        ''')
        results = cursor.fetchall()
        connect.close()
        return result;
    except NameError:
        print(NameError)