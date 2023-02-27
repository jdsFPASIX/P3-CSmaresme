import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash

################################INSERT
def nuevousuario(VALUES):
    conn = sqlite3.connect('maresme.sqlite')
    sql = '''
        INSERT INTO usuarios(nombre,apellido1,apellido2,fecha_nac,email,telefono,usuario,password) VALUES(?,?,?,?,?,?,?,?)
        '''
    pasword = VALUES[-1]
    VALUES[-1] = generate_password_hash(pasword)
    conn.execute(sql, VALUES)
    conn.commit()
    conn.close()

def nuevoarticulo(VALUES):

def nuevoprestamo(VALUES):
    conn = sqlite3.connect('maresme.sqlite')


###############################SELECT
def ver_usuarios(id=None):
    # 1. Conexitar bbdd
    conn = sqlite3.connect('maresme.sqlite')
    # 2. Escoger tipo de consulta para optimizar lectura entre 1 o todos los elementos
    if id is None:
        usuarios = conn.execute('SELECT *  FROM usuarios')
    else:
        usuarios = conn.execute('SELECT * FROM usuarios WHERE idusuario=?', [id])
    # 3. Guardar en una lista un diccionario por cada elemento
    list_usuarios = []
    for usuario in usuarios:
        list_usuarios.append(
            {
                'idarticulo': idusuario[0],
                'titulo': nombre[1],
                'autor': apellido1[2],
                'interprete': apellido2[3],
                'fecha_pub': fecha_nac[4],
                'categoria': email[5],
                'descripcion': telefono[6],
                'disponible': fecha_alta[7],
                'activo': usuario[8],
                'observaciones': articulo[9],
                'imagen1': articulo[10],
                'imagen2': articulo[11],
                'imagen3': articulo[12]
            }
        )
    # 4. Cerrar conexión bbdd y devolver lista
    connect_database.close()
    return list_articulos
def ver_articulos(id=None):
    # 1. Conexitar bbdd
    conn = sqlite3.connect('maresme.sqlite')
    # 2. Escoger tipo de consulta para optimizar lectura entre 1 o todos los elementos
    if id is None:
        articulos = conn.execute('SELECT *  FROM articulos')
    else:
        articulos = conn.execute('SELECT * FROM articulos WHERE idarticulo=?', [id])
    # 3. Guardar en una lista un diccionario por cada elemento
    list_articulos = []
    for articulo in articulos:
        list_articulos.append(
            {
                'idarticulo': articulo[0],
                'titulo': articulo[1],
                'autor': articulo[2],
                'interprete': articulo[3],
                'fecha_pub': articulo[4],
                'categoria': articulo[5],
                'descripcion': articulo[6],
                'disponible': articulo[7],
                'activo': articulo[8],
                'observaciones': articulo[9],
                'imagen1': articulo[10],
                'imagen2': articulo[11],
                'imagen3': articulo[12]
            }
        )
    # 4. Cerrar conexión bbdd y devolver lista
    connect_database.close()
    return list_articulos
def ver_prestamos(id=None):
    # 1. Conexitar bbdd
    conn = sqlite3.connect('maresme.sqlite')
    # 2. Escoger tipo de consulta para optimizar lectura entre 1 o todos los elementos
    if id is None:
        prestamos = conn.execute('SELECT *  FROM articulos')
    else:
        prestamos = conn.execute('SELECT * FROM prestamos WHERE idprestamo=?', [id])
    # 3. Guardar en una lista un diccionario por cada elemento
    list_prestamos = []
    for prestamo in prestamos:
        list_prestamos.append(
            {
                'idprestamo': articulo[0],
                'usuario': articulo[1],
                'articulo': articulo[2],
                'fecha_ini': articulo[3],
                'fecha_dev': articulo[4],
                'devuelto': articulo[5],
                'observaciones': articulo[9]
            }
        )
    # 4. Cerrar conexión bbdd y devolver lista
    connect_database.close()
    return list_prestamos