from flask_restful import Resource, reqparse

from models.model_contact import ContactModel


class Meta(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name')
    arguments.add_argument('phone')


class Contacts(Meta):
    def get(self):
        return {'message': 'retorna'}

    def post(self, ):
        data = Contacts.arguments.parse_args()
        if ContactModel.find_contact({'phone': data['phone'], 'contact_id': False}):
            return {'Message': f"The number sent already {data['phone']} exists"}
        try:
            new_contact = ContactModel(**data)
            new_contact.save_contact()
        except Exception as err:
            return {'Message': f'Ops!, error saving phone : {err}'}

        return new_contact.json()


class Contact(Meta):
    def get(self, contact_id):
        pass

    def put(self, contact_id):
        dados = Contacts.arguments.parse_args()
        print(dados)

    def delete(self, contact_id):
        pass
