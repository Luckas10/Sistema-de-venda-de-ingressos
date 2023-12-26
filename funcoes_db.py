import sqlite3 as db

def criar_banco(name_db):
    banco = db.connect(f"{name_db}.db")


def criar_tabela(table_name, name_db):
    banco = db.connect(f"{name_db}.db")

    cursor = banco.cursor()

    cursor.execute(f"CREATE TABLE {table_name} (id text, indice text, username text)")

    banco.commit()


def adicionar_user(table_name, name_db, values_users=()):
    banco = db.connect(f"{name_db}.db")

    cursor = banco.cursor()

    cursor.execute(f"INSERT INTO {table_name} VALUES {values_users}")

    banco.commit()


def listar_usuarios(table_name, name_db):
    banco = db.connect(f"{name_db}.db")

    cursor = banco.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    
    lista = cursor.fetchall()

    return lista

