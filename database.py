from flask import Flask
from flask_sqlalchemy import SQLAlchemy as db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "r'sqlite:////C:/Users/LENOVO/Desktop/Proyecto/user.db'"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
base = declarative_base()

class Users(db.model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(30))
    email = db.Colum(db.String(30))
    password = db.Colum(db.String(30))

    def __repr__(self):
        return "<User %r>"  % self.user 


if __name__ == "__main__":
    app.un(debug = True)