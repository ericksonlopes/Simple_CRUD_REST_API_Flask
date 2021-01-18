from sql_alchemy import db


class ContactModel(db.Model):
    __tablename__ = 'contacts'

    contact_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    # Função para retornar o objeto em json
    def json(self):
        return {
            'contact_id': self.contact_id,
            'name': self.name,
            'phone': self.phone
        }

    # classe método para procurar numero ou id
    @classmethod
    def find_contact_or_number(cls, find_dict):
        # se algum item for encontrado dentro  do item 'phone'
        if find_dict['phone']:
            # verifica se o número ja existe, buscando apenas 1 resultado
            find_phone = cls.query.filter_by(phone=find_dict['phone']).first()
            # se existir retorna o mesmo encontrado
            if find_phone:
                return find_phone

        # mesma função decima
        if find_dict['contact_id']:

            find_id = cls.query.filter_by(contact_id=find_dict['contact_id']).first()
            if find_id:
                return find_id

        # se nada for encontrado
        return False

    # Salvar contato
    def save_contact(self):
        # Pega o objeto e salva no banco
        db.session.add(self)
        # realiza o commit para salvar as alterações
        db.session.commit()

    # Deletar contato
    def delete_contact(self):
        # Pega o objeto para deletar no banco
        db.session.delete(self)
        # realiza o commit para salvar as alterações
        db.session.commit()

    # Atualiza contato
    def update_contact(self, name, phone):
        # Incrementa os novos dados nas variaveis obj
        self.name = name
        self.phone = phone
