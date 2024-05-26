'''
sqlite

sqlite3 database/tarefas.db
.databases
.tables
.exit
SELECT name from pragma_table_info('tarefas');
'''


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# servidor web de flask
app = Flask(__name__)
# para reinicializar o servidor sempre que alteramos o código
app.config["DEBUG"] = True
#app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database/tarefas.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../database/tarefas.db"
# cursor para a base de dados sqlite
db = SQLAlchemy(app)

class Tarefa(db.Model):
    __tablename__ = "tarefas"
    id = db.Column(db.Integer, primary_key=True) # Identificador único de cada
    # tarefa (não pode haver duas tarefas com o mesmo id, por isso é primary key)
    conteudo = db.Column(db.String(200)) # Conteúdo da tarefa, um texto de máximo200 caracteres
    feita = db.Column(db.Boolean) # Booleano que indica se uma tarefa foi feita ou não

with app.app_context(): #<- adicionar o contexto
    db.create_all() # Criação das tabelas
    db.session.commit() # Execução das tarefas pendentes da base de dados


@app.route('/')
def home():
    todas_as_tarefas = Tarefa.query.all() # Consultamos e armazenamos todas as tarefas da base de dados
    # Agora na variável todas_as_tarefas estão armazenadas todas as tarefas.Vamos entregar esta variável ao template index.html
    return render_template("index.html", lista_de_tarefas=todas_as_tarefas) # Carrega-se o template index.html


@app.route('/criar-tarefa', methods=['POST'])
def criar():
    conteudo_tarefa = request.form['conteúdo_tarefa'].strip()  # Remove espaços em branco
    if conteudo_tarefa:  # Verifica se o conteúdo não está vazio
        tarefa = Tarefa(conteudo=conteudo_tarefa, feita=False)
        db.session.add(tarefa)  # Adiciona a tarefa ao banco de dados
        db.session.commit()  # Executa a operação pendente da base de dados
    return redirect(url_for('home'))  # Redireciona-nos à função home()



@app.route('/eliminar-tarefa/<id>')
def eliminar(id):
    tarefa = Tarefa.query.filter_by(id=int(id)).first()  # Obtém a tarefa que se procura
    if tarefa:  # Verifica se a tarefa existe
        db.session.delete(tarefa)  # Remove a tarefa
        db.session.commit()  # Executa a operação pendente da base de dados
    return redirect(url_for('home'))  # Redireciona-nos à função home


@app.route('/tarefa-feita/<id>')
def feita(id):
    tarefa = Tarefa.query.filter_by(id=int(id)).first() # Obtém-se a tarefa que se procura
    tarefa.feita = not(tarefa.feita) # Guardar na variável booleana da tarefa, o seu contrário
    db.session.commit() # Executar a operação pendente da base de dados
    return redirect(url_for('home')) # Redireciona-nos para a função home()


app.run()