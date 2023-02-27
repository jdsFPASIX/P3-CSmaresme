from flask import *
import funcionesbbdd
#from fucttools import wrapper

app = Flask(__name__)
app.secret_key = 'akjdaklfbobjbfñjbfnljdñNLMcKDBFJñldfnñsFBOÑ'

@app.route('/')
def mostrar_home():
    return render_template('a1-home.html')
@app.route('/login')
def mostrar_login():
    return render_template('b1-login.html')
@app.route('/informacion')
def mostrar_informacion():
    return render_template('a2-informacion.html')
@app.route('/articulos', methods = ['GET', 'POST'])
def mostrar_articulos():
    if request.method == 'GET':
        articulos = funcionesbbdd.ver_articulos()
        return render_template('a3-articulos.html', articulos = articulos)
@app.route('/contacto')
def mostrar_contacto():
    return render_template('a4-contacto.html')


@app.route('/register', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        values = request.form.values()
        funcionesbbdd.nuevousuario(values)
        return redirect(url_for('mostrar_login'))


if __name__ == '__main__':
    app.run(debug='True')

