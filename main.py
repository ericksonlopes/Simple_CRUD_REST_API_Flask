from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_db.db'
api = Api(app)


@app.before_first_request
def create_database():
    db.create_all()


if __name__ == '__main__':
    from sql_alchemy import db

    db.init_app(app)
    app.run()
