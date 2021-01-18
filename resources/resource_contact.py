from flask_restful import Resource, reqparse

from models.model_contact import ContactModel


class Meta(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('phone')
    arguments.add_argument('name')


class Contacts(Meta):
    def get(self):
        return {'message': 'retorna'}

    def post(self):
        data = Contacts.arguments.parse_args()
        if ContactModel.find_contact(phone=data['phone']):
            return {'Message': "The number sent already exists"}
        try:


class Contact(Meta):
    def get(self, contact_id):
        pass

    def put(self, contact_id):
        dados = Contacts.arguments.parse_args()
        print(dados)

    def delete(self, contact_id):
        pass
