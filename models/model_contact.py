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
    def find_contact(cls, phone, contact_id):
        if contact_id is None:
            find_phone = cls.query.filter_by(phone=phone).first()
            if find_phone:
                return find_phone

        find_id = cls.query.filter_by(contact_id=contact_id)

        if find_id:
            return find_id
        return False

    def save_contact(self):
        db.session.add(self)
        db.session.commit()
