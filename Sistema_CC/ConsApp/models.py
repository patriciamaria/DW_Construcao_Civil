from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from ConsApp import db

class Usuario(db.Model):
    """Entidade Usuário"""
    id = db.Column(
        db.Integer,
        primary_key = True)

    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    senha = db.Column(db.String(100))
    tipo = db.Column(db.String(1))

    id_endereco = db.Column(
            db.Integer,
            db.ForeignKey('endereco.id'))

    endereco = db.relationship(
            'Endereco',
            backref='usuario',
            uselist=False)
    
    reservas = db.relationship(
            'Reserva',
            backref='usuario',
            lazy='dynamic')

    #Contrutor recebe os atributos nome, telefone e email.
    def __init__(self, nome, telefone, email, senha, tipo):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.tipo = tipo


class Endereco(db.Model):
    """Entidade Endereço Do Usuário"""
    id = db.Column(
        db.Integer,
        primary_key=True)

    cep = db.Column(db.String(10))
    cidade = db.Column(db.String(30))
    rua = db.Column(db.String(100))

    def __init__(self, cep, cidade, rua):
        self.cep = cep
        self.cidade = cidade
        self.rua = rua


produto_reserva = db.Table('produto_reserva',
    db.Column('id_produto', db.Integer, db.ForeignKey('produto.id')),
    db.Column('id_reserva', db.Integer, db.ForeignKey('reserva.id'))
)

class Reserva(db.Model):
    """Entidade Reserva"""
    id = db.Column(db.Integer, primary_key=True)    
    des_prod = db.Column(db.String(100))    
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    produtos = db.relationship(
        'Produto',
        secondary=produto_reserva,
        backref=db.backref(
        'reserva',
        lazy='dynamic'))
    
    def __init__(self, des_prod):
        self.des_prod = des_prod
    def __repr__(self):
        return '{} ({})'.format(self.des_prod, self.id_usuario)

class Produto(db.Model):
    """Entidade Produto"""
    id = db.Column(
        db.Integer,
        primary_key=True)

    nomep = db.Column(db.String(100))

    reservas = db.relationship(
        'Reserva',
        secondary=produto_reserva,
        backref=db.backref(
        'produto',
        lazy='dynamic'))

    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    def __init__(self, nomep):
        self.nomep = nomep
    def __repr__(self):
        return '{}'.format(self.nomep)

class Categoria(db.Model):
    """Entidade Categoria"""
    id = db.Column(
        db.Integer,
        primary_key=True)

    tipo = db.Column(db.String(100))
    descricao = db.Column(db.String(200))

    produtos = db.relationship('Produto', backref='categoria',
                                lazy='dynamic')
    def __init__(self, tipo, descricao):
        self.tipo = tipo
        self.descricao = descricao        
    def __repr__(self):
        return '{} ({})'.format(self.tipo, self.descricao)
        
