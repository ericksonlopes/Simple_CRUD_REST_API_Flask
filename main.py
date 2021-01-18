from flask import Flask
from flask_restful import Api

from resources.resource_contact import Contacts, Contact

app = Flask(__name__)
# configura a conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


# quando a primeira request for feita
@app.before_first_request
def create_database():
    # cria a estrutura e arquivo do banco de dados
    db.create_all()


# Caminho e recursos da aplicação
api.add_resource(Contacts, '/contacts')
api.add_resource(Contact, '/contact/contact_id')

if __name__ == '__main__':
    from sql_alchemy import db

    # inicia o banco de dados
    db.init_app(app)
    # inicia a aplicação se for chamada por esse arquivo

    app.run(debug=True)
