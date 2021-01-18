from flask_restful import Resource, reqparse

from models.model_contact import ContactModel


class Meta(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name')
    arguments.add_argument('phone')


class Contacts(Meta):
    def get(self):
        # retorna uma lista
        return {'All Contacts.': [contact.json() for contact in ContactModel.query.all()]}

    def post(self, ):
        # Juntas os itens recebido na request
        data = Contacts.arguments.parse_args()

        # Verifica se o item existe
        if ContactModel.find_contact_or_number({'phone': data['phone'], 'contact_id': False}):
            # Caso exista, retorna essa mensagem
            return {'Message': f"The number sent already {data['phone']} exists"}

        try:
            # Envia os dados para o construtor da classe
            new_contact = ContactModel(**data)
            # Tenta criar um novo contato
            new_contact.save_contact()
        except Exception as err:
            return {'Message': f'Ops!, error saving phone : {err}'}

        # Retorna o contato criado em json
        return new_contact.json()


class Contact(Meta):
    def get(self, contact_id):
        pass

    def put(self, contact_id):
        dados = Contacts.arguments.parse_args()
        print(dados)

    def delete(self, contact_id):
        find_contact = ContactModel.find_contact_or_number({'contact_id': contact_id, 'phone': False})

        if find_contact:
            try:
                find_contact.delete_contact()
                return {'message': f"Contact '{contact_id}' deleted!"}
            except Exception as error:
                return {'message': f'Internal error, {error}'}

        return {'message': 'Contact not found or deleted'}
