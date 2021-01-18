from flask_restful import Resource, reqparse

from models.model_contact import ContactModel


# classe meta para evitar duplicação de código
class Meta(Resource):
    # cria o objeto que recebe os dados da requests
    arguments = reqparse.RequestParser()
    # procura os seguintes itens
    arguments.add_argument('name')
    arguments.add_argument('phone')


class Contacts(Meta):
    def get(self):
        # retorna uma lista
        return {'All Contacts.': [contact.json() for contact in ContactModel.query.all()]}, 201

    def post(self, ):
        # Juntas os itens recebido na request
        data = Contacts.arguments.parse_args()

        # Verifica se o item existe
        if ContactModel.find_contact_or_number({'phone': data['phone'], 'contact_id': False}):
            # Caso exista, retorna essa mensagem
            return {'Message': f"The number sent already {data['phone']} exists"}, 404

        try:
            # Envia os dados para o construtor da classe
            new_contact = ContactModel(**data)
            # Tenta criar um novo contato
            new_contact.save_contact()
        except Exception as err:
            return {'Message': f'Ops!, error saving phone : {err}'}, 500

        # Retorna o contato criado em json
        return new_contact.json(), 200


class Contact(Meta):
    def get(self, contact_id):
        # Executa função que pesquisa o contact_id
        find_contact = ContactModel.find_contact_or_number({'contact_id': contact_id, 'phone': False})

        # se existir
        if find_contact:
            # retorna o objeto em json
            return find_contact.json(), 200

        return {'Message': "Contact not found"}, 404

    def put(self, contact_id):
        # Cria o objeto com os dados da requirição
        dados = Contacts.arguments.parse_args()

        # procura o id do contato
        find_contact = ContactModel.find_contact_or_number({'contact_id': contact_id, 'phone': False})

        # se for encontrado o contato requirido
        if find_contact:
            # Joga os novos dados recebido nas variaveis internas da classe
            find_contact.update_contact(**dados)
            try:
                # tenta salvar a alteração (o flask tem conhecimento suficiente para diferenciar salvar/modificar)
                find_contact.save_contact()
            except Exception as error:
                return {'message': f'Error updating contact, {error}'}, 500
            return find_contact.json(), 200

        # Caso não seja encontrado o contato, cria um novo
        try:
            # Joga os novos dados recebido nas variaveis internas da classe
            find_contact = ContactModel(**dados)
            # executa a função que slva os contatos
            find_contact.save_contact()

        except Exception as error:
            return {'message': f'Error saving contact, {error}'}
        # Retorna o ojb em forma de json
        return find_contact.json(), 201

    def delete(self, contact_id):
        # Executa função que pesquisa o contact_id
        find_contact = ContactModel.find_contact_or_number({'contact_id': contact_id, 'phone': False})

        # se for encontrado algo
        if find_contact:
            try:
                # tenta deletar o objeto retornado
                find_contact.delete_contact()
                return {'message': f"Contact '{contact_id}' deleted!"}, 201
            except Exception as error:
                # caso de erro ao salvar
                return {'message': f'Internal error, {error}'}, 500

        # Se não for encontrado retorna a mensagem
        return {'message': 'Contact not found or deleted'}
