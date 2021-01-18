from flask_restful import Resource


class Contacts(Resource):
    def get(self):
        return {'message': 'retornando todos'}


class Contact(Resource):
    pass
