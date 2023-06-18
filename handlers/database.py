import sqlite3 as sq

db = sq.connect('Chat-bot.db')



cur = db.cursor()

async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS Аккаунты("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "tg_id INTEGER)")

    cur.execute("CREATE TABLE IF NOT EXISTS ИКТСС("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "FIO TEXT, "
                "Возраст INTEGER, "
                "Адрес_проживания TEXT, "
                "Контактные_данные TEXT,"
                "Сумма_баллов INTEGER,"
                "Базовое_образование TEXT,"
                "Форма_обучения TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS ИВТ("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "FIO TEXT, "
                "Возраст INTEGER, "
                "Адрес_проживания TEXT, "
                "Контактные_данные TEXT,"
                "Сумма_баллов INTEGER,"
                "Базовое_образование TEXT,"
                "Форма_обучения TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS ИСиСС("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "FIO TEXT, "
                "Возраст INTEGER, "
                "Адрес_проживания TEXT, "
                "Контактные_данные TEXT,"
                "Средний_балл_за_аттестат TEXT,"
                "Базовое_образование TEXT,"
                "Форма_обучения TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS МТОиРЭПиУ("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "FIO TEXT, "
                "Возраст INTEGER, "
                "Адрес_проживания TEXT, "
                "Контактные_данные TEXT,"
                "Средний_балл_за_аттестат TEXT,"
                "Базовое_образование TEXT,"
                "Форма_обучения TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS ОИБАС("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "FIO TEXT, "
                "Возраст INTEGER, "
                "Адрес_проживания TEXT, "
                "Контактные_данные TEXT,"
                "Средний_балл_за_аттестат TEXT,"
                "Базовое_образование TEXT,"
                "Форма_обучения TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS СиСА("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "FIO TEXT, "
                "Возраст INTEGER, "
                "Адрес_проживания TEXT, "
                "Контактные_данные TEXT,"
                "Средний_балл_за_аттестат TEXT,"
                "Базовое_образование TEXT,"
                "Форма_обучения TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS ИСиП("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "FIO TEXT, "
                "Возраст INTEGER, "
                "Адрес_проживания TEXT, "
                "Контактные_данные TEXT,"
                "Средний_балл_за_аттестат TEXT,"
                "Базовое_образование TEXT,"
                "Форма_обучения TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS ПС("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "FIO TEXT, "
                "Возраст INTEGER, "
                "Адрес_проживания TEXT, "
                "Контактные_данные TEXT,"
                "Средний_балл_за_аттестат TEXT,"
                "Базовое_образование TEXT,"
                "Форма_обучения TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS ЭиБУ("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "FIO TEXT, "
                "Возраст INTEGER, "
                "Адрес_проживания TEXT, "
                "Контактные_данные TEXT,"
                "Средний_балл_за_аттестат TEXT,"
                "Базовое_образование TEXT,"
                "Форма_обучения TEXT)")
    db.commit()

async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM Аккаунты WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO Аккаунты (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()

async def zapolnenieIKTSS(FIO,age,adress,score, contact, obrazovanie, forma_obuch):
    cur.execute('''INSERT INTO ИКТСС (FIO, Возраст, Адрес_проживания, Контактные_данные, Сумма_баллов, Базовое_образование, Форма_обучения)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (FIO, age, adress, contact, score, obrazovanie, forma_obuch))
    db.commit()
async def zapolnenieIVT(FIO,age,adress,contact, score, obrazovanie, forma_obuch):
    cur.execute('''INSERT INTO ИВТ (FIO, Возраст, Адрес_проживания, Контактные_данные, Сумма_баллов, Базовое_образование, Форма_обучения)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (FIO, age, adress, contact, score, obrazovanie, forma_obuch))
    db.commit()
async def zapolnenieISSS(FIO,age,adress,score, contact, obrazovanie, forma_obuch):
    cur.execute('''INSERT INTO ИСиСС (FIO, Возраст, Адрес_проживания, Контактные_данные, Средний_балл_за_аттестат, Базовое_образование, Форма_обучения)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (FIO, age, adress, contact, score, obrazovanie, forma_obuch))
    db.commit()
async def zapolnenieMTOREBU(FIO,age,adress,score, contact, obrazovanie, forma_obuch):
    cur.execute('''INSERT INTO МТОиРЭПиУ (FIO, Возраст, Адрес_проживания, Контактные_данные, Средний_балл_за_аттестат, Базовое_образование, Форма_обучения)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (FIO, age, adress, contact, score, obrazovanie, forma_obuch))
    db.commit()
async def zapolnenieSSA(FIO,age,adress,score, contact, obrazovanie, forma_obuch):
    cur.execute('''INSERT INTO СиСА (FIO, Возраст, Адрес_проживания, Контактные_данные, Средний_балл_за_аттестат, Базовое_образование, Форма_обучения)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (FIO, age, adress, contact, score, obrazovanie, forma_obuch))
    db.commit()
async def zapolnenieISP(FIO,age,adress,score, contact, obrazovanie, forma_obuch):
    cur.execute('''INSERT INTO ИСиП (FIO, Возраст, Адрес_проживания, Контактные_данные, Средний_балл_за_аттестат, Базовое_образование, Форма_обучения)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (FIO, age, adress, contact, score, obrazovanie, forma_obuch))
    db.commit()
async def zapolneniePS(FIO,age,adress,score, contact, obrazovanie, forma_obuch):
    cur.execute('''INSERT INTO ПС (FIO, Возраст, Адрес_проживания, Контактные_данные, Средний_балл_за_аттестат, Базовое_образование, Форма_обучения)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (FIO, age, adress, contact, score, obrazovanie, forma_obuch))
    db.commit()
async def zapolnenieEBU(FIO,age,adress,score, contact, obrazovanie, forma_obuch):
    cur.execute('''INSERT INTO ЭиБУ (FIO, Возраст, Адрес_проживания, Контактные_данные, Средний_балл_за_аттестат, Базовое_образование, Форма_обучения)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (FIO, age, adress, contact, score, obrazovanie, forma_obuch))
    db.commit()
async def zapolnenieOIBAS(FIO,age,adress,score, contact, obrazovanie, forma_obuch):
    cur.execute('''INSERT INTO ОИБАС (FIO, Возраст, Адрес_проживания, Контактные_данные, Средний_балл_за_аттестат, Базовое_образование, Форма_обучения)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (FIO, age, adress, contact, score, obrazovanie, forma_obuch))
    db.commit()
async def zapolnenieAdmins(user_id,username):
    cur.execute("INSERT INTO admins (user_id,username) VALUES (?,?)", (user_id,username))
    db.commit()