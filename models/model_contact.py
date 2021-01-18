from sql_alchemy import db


class ContactModel(db.Model):
    __tablename__ = 'contacts'

    contact_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.Integer, unique=True)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


