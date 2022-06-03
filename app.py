# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_templates

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World' render_templates('index.html', clientes=clientes)
app.run(debug=True)

print('Olá mundo')