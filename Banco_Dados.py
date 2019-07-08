import sqlite3

conectar = sqlite3.connect('BancoDados.db')

cursor = conectar.cursor()

conectar.execute("""
CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

print('O programa foi conectado ao banco de dados')
