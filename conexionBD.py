import sqlite3 as sql
import os

# Specify path
path_bd = 'whatsaapBot.db'

# validamos si existe el archivo de bases de datos

isExist = os.path.exists(path_bd)

if isExist:
    pass
else:
    try:
        con = sql.connect("whatsaapBot.db")
        cursor = con.cursor()

        # Creamos las Tablas
        cursor.execute('''
                               CREATE TABLE IF NOT EXISTS BOT_RESPONSE(
                               RESPONSE_BOT TEXT,
                               COD_RESPONSE INTEGER NOT NULL)
                               ''')

        cursor.execute('''
                               CREATE TABLE IF NOT EXISTS USER_QUESTION(
                               MESSAGE_USER TEXT,
                               COD_RESPONSE_BOT INTEGER NOT NULL)
                               ''')

        con.commit()
        con.close()
    except:
        print("Error en la base de datos...")

def lst_question():

    try:
        con = sql.connect("whatsaapBot.db")
        cursor = con.cursor()
        sql_sintaxis = "SELECT DISTINCT COD_RESPONSE_BOT FROM USER_QUESTION ORDER BY COD_RESPONSE_BOT ASC"
        cursor.execute(sql_sintaxis)
        question = cursor.fetchall()
        lst_question = []

        for fila in question:
            for columna in fila:
                lst_question.append(columna)
        return lst_question
    except:
        print("Error en la base de datos...")

def user_question(id):

    try:
        con = sql.connect("whatsaapBot.db")
        cursor = con.cursor()
        sql_sintaxis = f"SELECT MESSAGE_USER FROM USER_QUESTION WHERE COD_RESPONSE_BOT = '{id}'"
        cursor.execute(sql_sintaxis)
        fromCursor = cursor.fetchall()
        lst_user_question = []

        for fila in fromCursor:
            for columna in fila:
                lst_user_question.append(columna)
        return lst_user_question
    except:
        print("Error en la base de datos...")

def response_bot(id):

    try:
        con = sql.connect("whatsaapBot.db")
        cursor = con.cursor()
        sql_sintaxis = f"SELECT RESPONSE_BOT FROM BOT_RESPONSE WHERE COD_RESPONSE = '{id}'"
        cursor.execute(sql_sintaxis)
        fromCursor = cursor.fetchall()
        lst_bot_response = []

        for fila in fromCursor:
            for columna in fila:
                lst_bot_response.append(columna)
        return lst_bot_response
    except:
        print("Error en la base de datos...")


def register(nombre, password, apellido, direccion, comentario):

    con = sql.connect("whatsaapBot.db")
    cursor = con.cursor()
    sql_sintaxis = f"INSERT INTO USUARIOS VALUES (NULL,'{nombre}', '{password}', '{apellido}'," \
                  f"'{direccion}', '{comentario}')"
    cursor.execute(sql_sintaxis)
    con.commit()
    con.close()