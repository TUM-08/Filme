from db import db

class filme(db.Model):
    __tablename__ = 'filme'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False)
    genero = db.Column(db.String(80), nullable=False)
    duracao = db.Column(db.Integer, nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    diretor = db.Column(db.String(80), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'duracao': self.duracao,
            'ano': self.ano,
            'diretor': self.diretor
        }