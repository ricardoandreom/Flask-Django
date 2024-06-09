from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'))


class Vehicle(db.Model):
    __tablename__ = 'veiculos'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    valor_diaria = db.Column(db.Float, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    data_ultima_revisao = db.Column(db.Date, nullable=False)
    data_proxima_revisao = db.Column(db.Date, nullable=False)
    data_ultima_inspecao = db.Column(db.Date, nullable=False)
    disponivel = db.Column(db.String(3), nullable=False, default='Sim')
    transmissao = db.Column(db.String(100), nullable=False)
    categoria_quantidade = db.Column(db.String(100), nullable=False)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'))


class Reservation(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    data_reserva = db.Column(db.Date, nullable=False)
    forma_pagamento = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100), nullable=False)
    morada = db.Column(db.String(200), nullable=False)
    valor = db.Column(db.Float(10, 2), nullable=False)

