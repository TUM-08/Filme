from models.filme_models import filme
from db import db
import json
from flask import make_response

def create_filme(filme_data):
    novo_filme = filme(
        titulo=filme_data['titulo'],
        genero=filme_data['genero'],
        duracao=filme_data['duracao'],
        ano=filme_data['ano'],
        diretor=filme_data['diretor']
    )

    db.session.add(novo_filme)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'Filme cadastrado com sucesso.',
            'filme': novo_filme.json()
        }, sort_keys=False)
    )

    response.headers['Content-Type'] = 'application/json'
    return response