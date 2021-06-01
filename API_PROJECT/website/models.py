from sqlalchemy.orm import relationship
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default = func.now()) #usamos el metodo func.now para que sqlalchemy se encargue y nos actualice la hora automaticamente.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #llave foranea para obtener el id de los usuarios.

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #llave primaria ID
    email = db.Column(db.String(150), unique=True) #Email como columna unica(no pueden haber 2 registros con el mismo email)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #este campo almacena todas las notas de usuario o cuales posee.
    __tablename__ = 'user'