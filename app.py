from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import csv
import json

app = Flask('__name__')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        fields = json.loads(request.args.get('fields').replace("'", '"'))
        return render_template('create.html', fields=fields)
    elif request.method == 'POST':
        data = dict(request.form)

        with open('computador.csv', 'a') as mais:
            writer = csv.DictWriter(mais, fieldnames=data.keys())
            writer.writerow(data)
        return redirect('/')

@app.route('/')
def read():
    data = []

    with open('computador.csv') as ler:
        reader = csv.DictReader(ler)
        for row in reader:
            data.append(dict(row))
    return render_template('index.html', data=data, list=list, len=len, str=str)

@app.route('/delete')
def delete():
    with open('computador.csv') as deletar:
        data = []
        temp_data = []
        reader = csv.DictReader(deletar)

        for row in reader:
            temp_data.append(dict(row))
        [
            data.append(temp_data[row])
            for row in range(0, len(temp_data))
            if row != int(request.args.get('id'))
        ]

        with open('computador.csv', 'w') as editar:
            writer = csv.DictWriter(editar, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    return redirect('/')

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        data = []

        with open('computador.csv') as atualizar:
            reader = csv.DictReader(atualizar)
            for row in reader:
                data.append(dict(row))

            return render_template('update.html', fields=data[int(request.args.get('id'))])

    elif request.method == 'POST':
        data = []

    with open('computador.csv') as identificar:
        reader = csv.DictReader(identificar)
        for row in reader:
            data.append(dict(row))
        row = {}

        for key, val in dict(request.form).items():
            if key != 'Id':
                row[key] = val

        data[int(request.form.get('Id'))] = row

        with open('computador.csv', 'w') as edicao:
            writer = csv.DictWriter(edicao, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        return redirect('/')

app.run(debug=True)
