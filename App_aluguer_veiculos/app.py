from flask import Flask,  render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'  # Substitua com a sua chave secreta gerada
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

with app.app_context(): # <- adicionar o contexto
    db.create_all() # Criação das tabelas
    db.session.commit() # Execução das tarefas pendentes da base de dados

from routes import *


def atualizar_disponibilidade_veiculos():
    # Obter a data atual
    data_atual = datetime.now().date()
    # Calcular a data limite de 1 ano atrás
    data_limite = data_atual - timedelta(days=365)

    # Buscar todos os veículos
    veiculos = Vehicle.query.all()

    for veiculo in veiculos:
        # Verificar se a data da última inspeção é maior que 1 ano
        if veiculo.data_ultima_inspecao < data_limite:
            veiculo.disponivel = "Não"
        # Verificar se a data da próxima revisão é anterior à data atual
        elif veiculo.data_proxima_revisao < data_atual:
            veiculo.disponivel = "Não"
        else:
            veiculo.disponivel = "Sim"

    # Commitar as alterações na base de dados
    db.session.commit()


# Adicione isso no final NO `app.py`
if __name__ == '__main__':
    with app.app_context():
        atualizar_disponibilidade_veiculos()
    app.run(debug=True)




