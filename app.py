from flask import *


app = Flask(__name__)

@app.route('/')
def hello_world(): # put application's code here
    return render_template('template_index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contacto')
def contacto():
    return render_template('Contacto.html')

caca caca caca caca



if __name__ == '__main__':
    app.run(debug='True')

