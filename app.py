from flask import *


app = Flask(__name__)

@app.route('/')
def hello_world(): # put application's code here

    return render_template('template_index.html')


"""if __name__ == '__main__':
    app.run(debug='True')"""




