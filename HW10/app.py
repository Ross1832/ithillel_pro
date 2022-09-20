from avg_data import avg_height, avg_kg
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/avr_data')
def get_avr_data():
    return f"From hw.csv file the average parameters are:</br>" \
           f"Height {avg_height()} cm</br>" \
           f"Weight {avg_kg()} kg"


@app.route('/requirements')
def get_requirements():
    a = []
    with open('requirements.txt', 'r') as f:
        for i in f.readlines():
            a.append(i)
    return '<br/>'.join(a)


app.run(port=5000, debug=True)
