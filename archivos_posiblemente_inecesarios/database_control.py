import sqlite3

def create_scheme():
    print('El esquema se extrae de sqlite Studio')
def insert_massive_data():
    print('insertando datos')
def deleteall_data():
    print('borrando datos')

conn = sqlite3.connect('../maresme.sqlite')
conn.commit()
conn.close()
