
from flask import Flask, render_template, request, redirect, session
import json
import datetime
import os

app = Flask(__name__)
app.secret_key = 'chave-secreta-doguera'

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        with open('usuarios.json', 'r', encoding='utf-8') as f:
            usuarios = json.load(f)
        if nome in usuarios and usuarios[nome]['senha'] == senha:
            session['usuario'] = nome
            return redirect('/admin' if nome == 'admin' else '/cursos')
        else:
            return render_template('login.html', erro='Usuário ou senha inválidos.')
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        with open('usuarios.json', 'r', encoding='utf-8') as f:
            usuarios = json.load(f)
        if nome in usuarios:
            return render_template('cadastro.html', erro='Usuário já existe.')
        usuarios[nome] = {"senha": senha}
        with open('usuarios.json', 'w', encoding='utf-8') as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
        return redirect('/login')
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/login')

@app.route('/cursos')
def cursos():
    if 'usuario' not in session or session['usuario'] == 'admin':
        return redirect('/login')
    return render_template('cursos_fase1_completo_integrado.html', usuario=session['usuario'])

@app.route('/registro', methods=['POST'])
def registrar_resultado():
    data = request.get_json()
    with open('resultados.json', 'r', encoding='utf-8') as f:
        resultados = json.load(f)
    data['data'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    resultados.append(data)
    with open('resultados.json', 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)
    return {'status': 'ok'}

@app.route('/admin')
def admin():
    if 'usuario' not in session or session['usuario'] != 'admin':
        return redirect('/login')
    with open('resultados.json', 'r', encoding='utf-8') as f:
        resultados = json.load(f)
    return render_template('admin.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
