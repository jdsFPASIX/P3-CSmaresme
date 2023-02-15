import sqlite3

def nuevousuario(nombre_nuevoingrediente):
    conn = sqlite3.connect('maresme.sqlite')
    sql = '''
        INSERT INTO usuarios(nombre) VALUES(?)
        '''
    VALUES = [nombre_nuevoingrediente]
    cursor = conn.execute(sql,VALUES)

    conn.commit()
    conn.close()