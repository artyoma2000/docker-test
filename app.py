# Импорт необходимых библиотек
import os
import random
import string
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Инициализация Flask приложения
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@db/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Определение модели данных
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


# Маршрут главной страницы
@app.route('/')
def index():
    return render_template('index.html')


# Маршрут для генерации и сохранения учетных данных
@app.route('/generate', methods=['POST'])
def generate():
    db.create_all()
    login = ''.join(random.choices(string.ascii_lowercase, k=10))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    account = Account(login=login, password=password)
    db.session.add(account)
    db.session.commit()
    return jsonify({'login': login, 'password': password, 'message': 'Account saved'})


# Маршрут для отображения всех учетных записей
@app.route('/accounts', methods=['GET'])
def accounts():
    db.create_all()
    accounts = Account.query.all()
    return jsonify([{'login': account.login, 'password': account.password} for account in accounts])


# Точка входа в приложение
if __name__ == '__main__':
    app.run(debug=True)
