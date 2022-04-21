from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SSECRET_KEY'] = 'asdjfyjahfıalfg jsafıasf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Kodu koştuğumda çıkan uyarı için.
db = SQLAlchemy(app)
api = Api(app)

if __name__ == "__main__":
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)