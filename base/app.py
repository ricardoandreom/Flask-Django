from flask import Flask,  render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'  # Substitua com sua chave secreta gerada
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

with app.app_context(): #<- adicionar o contexto
    db.create_all() # Criação das tabelas
    db.session.commit() # Execução das tarefas pendentes da base de dados

from routes import *

if __name__ == '__main__':
    app.run(debug=True)



