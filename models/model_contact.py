from sql_alchemy import db


class ContactModel(db.Model):
    __tablename__ = 'contacts'

    contact_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.Integer, unique=True)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def json(self):
        return {
            'contact_id': self.contact_id,
            'name': self.name,
            'phone': self.phone
        }

    @classmethod
    def find_contact_or_number(cls, find_dict):
        # se algum item for encontrado dentro  do item 'phone'
        if find_dict['phone']:
            # verifica se o número ja existe
            find_phone = cls.query.filter_by(phone=find_dict['phone']).first()
            # se existir retorna o mesmo encontrado
            if find_phone:
                return find_phone

        # mesma função decima
        if find_dict['contact_id']:
            find_id = cls.query.filter_by(contact_id=find_dict['contact_id'])
            if find_id:
                return find_id

        # se nada for encontrado
        return False

    def save_contact(self):
        db.session.add(self)
        db.session.commit()
