from flask import url_for, request, render_template, redirect, Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogos.db'
db = SQLAlchemy(app)

class Jogo(db.Model):
    __tablename__ = 'jogos'
    codigo = db.Column(db.String, primary_key=True, nullable=False)
    nome = db.Column(db.String, unique=False, nullable=False)
    desenvolvedor = db.Column(db.String, unique=False, nullable=False)
    ano = db.Column(db.String, unique=False, nullable=False)
    nota = db.Column(db.Float, unique=False, nullable=False)
    valor = db.Column(db.Float, unique=False, nullable=False)
    
    def __init__(self,codigo, nome,desenvolvedor,ano,nota,valor):
        self.codigo = codigo
        self.nome = nome
        self.desenvolvedor = desenvolvedor
        self.ano = ano
        self.nota = nota
        self.valor = valor

db.create_all()