# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template

app = Flask(__name__)

clientes = [

    {'nome': 'TESTE', 'comentario': 'OI'}
]

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/create')
def create():
    return render_template('create.html')

app.run(debug=True)
