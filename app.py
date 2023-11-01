import os

from flask import Flask, render_template

app = Flask(__name__)

os.environ['FLASK_DEBUG']='True'

app.debug = os.environ.get('FLASK_DEBUG')== 'True'

@app.route('/')
def ola():

    return render_template('index.html')
if __name__ == "__main__":
    app.run()